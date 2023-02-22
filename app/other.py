from flask import Blueprint,jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

other_api = Blueprint('other', __name__, url_prefix='/api/other')

# GET
@other_api.route('/', methods=['GET'])
@jwt_required()
def get_jwt():
    print("get_jwt hit!")
    return jsonify({'message': 'get_jwt','status': '0'})

# POST