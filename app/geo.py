from flask import Blueprint
from flask import jsonify
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
import os,dotenv
from modules.geo_fetch import fetcher

dotenv.load_dotenv()

geo_api = Blueprint('geo', __name__, url_prefix='/api/geo')

#目前先觀察資費

# @geo_api.route('/', methods=['GET'])
# @jwt_required()
# def get_geo():
#     max_retries = 2  # max retry
#     fetch_result = None
#     for _ in range(max_retries):
#         fetch_result = fetcher()
#         if fetch_result is not None:
#             break

#     if fetch_result is None:
#         return jsonify({"error": "Failed to fetch data after retries."}), 500
    
#     # upload img to s3 from img url
#     # Send notifit to TG and monitor route
#     return jsonify(fetch_result)