from flask import Blueprint
from flask import jsonify
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
import os,dotenv

dotenv.load_dotenv()

apod_api = Blueprint('apod', __name__, url_prefix='/api/apod')

@apod_api.route('/', methods=['GET'])
def get_apod():
    print("get_apod hit!")
    return jsonify({'message': 'get_apod','status': '0'})