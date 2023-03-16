from flask import Blueprint,jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
import os,dotenv

dotenv.load_dotenv()

board_api = Blueprint('board', __name__, url_prefix='/api/board')

client = MongoClient(os.getenv('DB_CONNECTION_DATA'))
messages_db = client["chi_vio_db"]["messages"]

@board_api.route('/', methods=['POST'])
@jwt_required()
def post_board():
    message = {
        'title': request.json.get('title'),
        'text': request.json.get('text')
    }
    try:
        messages_db.insert_one(message)
        return jsonify({'message': 'post_board','status': '0'})

    except Exception as e:
        print(e)
        return jsonify({'message': 'post_board','status': '1'})