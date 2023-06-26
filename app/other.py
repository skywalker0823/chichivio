from flask import Blueprint,jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
import os, dotenv

dotenv.load_dotenv()

other_api = Blueprint('other', __name__, url_prefix='/api/other')

client = MongoClient(os.getenv('DB_CONNECTION_DATA'))

# GET
@other_api.route('/', methods=['GET'])
@jwt_required()
def get_jwt():
    username = get_jwt_identity()
    try:
        query = {"username": username}
        result = client["chi_vio_db"]["users"].find_one(query)
        print(result)
        if result:
            return jsonify({'message': 'get_jwt','status': '0','username': username})
        else:
            return jsonify({'message': 'get_jwt','status': '1'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'db_test','status': '1'})



