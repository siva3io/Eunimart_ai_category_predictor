
import logging
import json
# from google.cloud import storage
import os
import boto3
from config import Config

boto3_session = boto3.session.Session(
            aws_access_key_id=Config.BOTO3_ACCESS_KEY,
            aws_secret_access_key=Config.BOTO3_SECRET_KEY)
s3 = boto3_session.resource('s3')

def catch_exceptions(func):
    def wrapped_function(*args, **kargs):
        try:
            return func(*args, **kargs)
        except Exception as e:
            l = logging.getLogger(func.__name__)
            l.error(e, exc_info=True)
            return None                
    return wrapped_function

"""
As storge is shifted to AWS s3 bucket, changed code to download from s3 instead of google storage.
"""

def download_from_s3(source_path,destination_path):
    s3.Bucket(Config.BOTO3_BUCKET).download_file(source_path,destination_path)

'''
def download_from_google_storage(bucket_name,source_blob_name,destination_file_name):
    """Downloads a blob from the bucket."""
   
    destination_dir = '/'.join(destination_file_name.split('/')[:-1])
    os.makedirs(destination_dir, exist_ok=True)
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

'''