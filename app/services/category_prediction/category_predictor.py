import numpy as np
from PIL import Image
import tensorflow as tf
import logging
import requests
from io import BytesIO
import base64
import os
from constants import model_name_id_map,error_codes,marketplace_vdezi_mapping,channel_id_name_mapping,cat_sub_cat_abbreviations,NA_model_names
from app.utils import catch_exceptions,download_from_s3
from config import Config
import json
import pandas as pd
from urllib.parse import urlparse

logger = logging.getLogger(name=__name__)

class GetCategory(object):

    def __init__(self):
        pass

    @catch_exceptions
    def load_labels(self,filename):
        try:
            with open(filename, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except Exception as e:
            logger.error(e,exc_info=True)
    
    @catch_exceptions
    def get_image(self,image):
        try:
            parsed_image = urlparse(image)
            if all([parsed_image.scheme, parsed_image.netloc, parsed_image.path]):
                response = requests.get(image,  headers={"User-Agent": "XY"})
                img = Image.open(BytesIO(response.content))
            else:
                bytes_string = base64.b64decode(image)
                img = Image.open(BytesIO(bytes_string))
            if img.mode in ("RGBA", "P"):     #https://stackoverflow.com/questions/48206051/image-conversion-cannot-write-mode-rgba-as-jpeg
                img = img.convert("RGB")
            return img
        except Exception as e:
            logger.error(e,exc_info=True)
            return ''
    
    @catch_exceptions
    def get_file_paths(self,marketplace,model_name):
        try:
            path = os.getcwd()
            model_file = marketplace+'/'+model_name+'/model.tflite'
            abs_model_file_path = path +'/'+model_file
            if not os.path.exists(abs_model_file_path):
                os.makedirs(str(path + '/' + marketplace + '/' + model_name), exist_ok=True)
                download_from_s3(str("category_predictor/"+model_file),abs_model_file_path)
            label_file = marketplace+'/'+model_name+'/dict.txt'
            abs_label_file_path = path + '/' + label_file
            if not os.path.exists(abs_label_file_path):
                os.makedirs(str(path + '/' + marketplace + '/' + model_name), exist_ok=True)
                download_from_s3(str("category_predictor/"+label_file),abs_label_file_path)
            return abs_model_file_path,abs_label_file_path
        except Exception as e:
            logger.error(e,exc_info=True)
    
    @catch_exceptions
    def get_abbreviations(self,marketplace,abbreviated_category,abbreviated_sub_category):
        try:
            category_name = cat_sub_cat_abbreviations.get(marketplace).get(abbreviated_category).get(abbreviated_sub_category).get("category_name")
            sub_category_name = cat_sub_cat_abbreviations.get(marketplace).get(abbreviated_category).get(abbreviated_sub_category).get("sub_category_name")
            return category_name, sub_category_name
        except Exception as e:
            logger.error(e,exc_info=True)

    @catch_exceptions
    def get_category(self,request_data,model_name,image):
        try:
            model_file_path,label_file_path = self.get_file_paths(request_data["marketplace"],model_name)
            input_mean = 127.5
            input_std = 127.5
            interpreter = tf.lite.Interpreter(model_path=model_file_path)
            interpreter.allocate_tensors()
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()
            floating_model = input_details[0]['dtype'] == np.float32
            height = input_details[0]['shape'][1]
            width = input_details[0]['shape'][2]
            resized_image = image.resize((width, height))
            input_data = np.expand_dims(resized_image, axis=0)
            if floating_model:
                input_data = (np.float32(input_data) - input_mean) / input_std
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])
            results = np.squeeze(output_data)
            top_k = results.argsort()[-1:][::-1]
            labels = self.load_labels(label_file_path)
            category = labels[top_k[0]]
            return category
        except Exception as e:
            logger.error(e,exc_info=True)

    @catch_exceptions
    def predict_marketplace_hierarchy(self,request_data,image):
        abbreviated_category = self.get_category(request_data,model_name_id_map.get(request_data["marketplace"]).get('Level_0_Images'),image)
        print("abbreviated_category==>",abbreviated_category)
        if model_name_id_map[request_data["marketplace"]][abbreviated_category] == 'NA':
            abbreviated_sub_category = NA_model_names[request_data["marketplace"]][abbreviated_category]
        else:
            abbreviated_sub_category = self.get_category(request_data,model_name_id_map.get(request_data["marketplace"]).get(abbreviated_category),image)
        print("abbreviated_sub_category==>",abbreviated_sub_category)
        category,sub_category= self.get_abbreviations(request_data["marketplace"],abbreviated_category,abbreviated_sub_category)
        print("category==>",category)
        print("sub_category==>",sub_category)
        return category,sub_category

    @catch_exceptions
    def get_marketplace_hierarchy(self,request_data):
        print("request_data==>",request_data)
        response_data = {}
        mandatory_fields = ["image","channel_id"]
        for field in mandatory_fields:
            if not field in request_data["data"]:
                response_data = {
                    "status":False,
                    "message":"Required field is missing",
                    "error_obj":{
                        "description":"{} is missing".format(field),
                        "error_code":"REQUIRED_FIELD_IS_MISSING"
                    }
                }
        if not response_data:
            request_data["data"]["marketplace"] = channel_id_name_mapping.get(request_data["data"]["channel_id"])
            image = self.get_image(request_data["data"]["image"])
            if image:
                category,sub_category = self.predict_marketplace_hierarchy(request_data["data"],image)
                response_data = {
                    "status":True,
                    "message":"Category Prediction completed",
                    "data":
                    {
                        "category_name":category,
                        "sub_category_name":sub_category
                    }
                }
            else:
                response_data = {
                    "status":False,
                    "message":"Image is not valid",
                    "error_obj":{
                        "description":"Image is not valid",
                        "error_code":"INVALID_IMAGE"
                    }
                }

        return response_data

    @catch_exceptions
    def get_vdezi_hierarchy(self,request_data):
        request_data["data"]["channel_id"] = "12"
        marketplace_response = self.get_marketplace_hierarchy(request_data)
        if marketplace_response.get("error_obj"):
            return marketplace_response
        else:
            category = marketplace_response["data"]["category_name"]
            sub_category = marketplace_response["data"]["sub_category_name"]
            response_data = {
                "status":True,
                "message":"Category Prediction completed",
                "data":marketplace_vdezi_mapping.get(category).get(sub_category)
            }
            return response_data


CategoryPrediction = GetCategory()