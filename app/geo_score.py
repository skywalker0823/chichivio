from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity


geo_score_api = Blueprint('geo_score', __name__, url_prefix='/api/geo_score')

# 使用 Redis 做即時記分板

@geo_score_api.route('/', methods=['GET'])
def geo_score():
    return