from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, set_access_cookies, verify_jwt_in_request
# from pymongo import MongoClient
import os, dotenv
from database.planet_scale import DB

dotenv.load_dotenv()

database = DB()
signup_api = Blueprint('signin_api', __name__, url_prefix='/api/signup')

# client = MongoClient(os.getenv('DB_CONNECTION_DATA'))



@signup_api.route('/', methods=['POST'])
def signup():
    print(request.json,"signup hit!")
    username = request.json['username']
    password = request.json['password']
    try:
        result = database.get_user(username,password)
        if result:
            return jsonify({'message': 'signup','status': '1'})
        else:
            database.insert_user(username,password)
            response = jsonify({'message': 'signup','status': "0"})
            access_token = create_access_token(identity=username)
            set_access_cookies(response, access_token)
            return response
    except Exception as e:
        print(e)
        return jsonify({'message': 'db_test','status': '1'})



# @signin_api.route('/', methods=['POST'])
# def signin():
#     print(request.json,"signin hit!")
#     username = request.json['username']
#     password = request.json['password']
#     try:
#         query = {"username": username}
#         result = client["chi_vio_db"]["users"].find_one(query)
#         if result:
#             return jsonify({'message': 'signin','status': '1'})
#         else:
#             client["chi_vio_db"]["users"].insert_one({"username": username, "password": password})
#             response = jsonify({'message': 'signin','status': "0"})
#             access_token = create_access_token(identity=username)
#             set_access_cookies(response, access_token)
#             return response
#     except Exception as e:
#         print(e)
#         return jsonify({'message': 'db_test','status': '1'})