from flask import Blueprint,jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

member_api = Blueprint('member', __name__, url_prefix='/api/member')

# GET
@member_api.route('/', methods=['GET'])
@jwt_required()
def get_member():
    print("get_member hit!")
    return jsonify({'message': 'get_member','status': '0'})

# POST
@member_api.route('/', methods=['POST'])
@jwt_required()
def post_member():
    print("post_member hit!")
    return jsonify({'message': 'post_member','status': '0'})