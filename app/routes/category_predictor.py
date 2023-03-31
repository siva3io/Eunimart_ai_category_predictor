import logging
from flask import Blueprint, jsonify, request
from app.services.category_prediction import CategoryPrediction

category_predictor = Blueprint('category_predictor', __name__)

logger = logging.getLogger(__name__)


@category_predictor.route('/predict_marketplace', methods=['POST'])
def get_marketplace_hierarchy():
    request_data = request.get_json()
    data = CategoryPrediction.get_marketplace_hierarchy(request_data)
    if not data:
        data = {}
    return jsonify(data)

@category_predictor.route('/predict_vdezi', methods=['POST'])
def get_vdezi_hierarchy():
    request_data = request.get_json()
    data = CategoryPrediction.get_vdezi_hierarchy(request_data)
    if not data:
        data = {}
    return jsonify(data)
