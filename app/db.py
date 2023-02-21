from flask import Blueprint,jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, set_access_cookies


db_api = Blueprint('db', __name__, url_prefix='/api/db')

# RESTful API

# POST
@db_api.route('/login', methods=['POST'])
def login():
    print(request.json,"login hit!")
    username = request.json['username']
    password = request.json['password']
    print(username,password)
    if username == '123' and password == '123':
        response = jsonify({'message': 'login','status': "0"})
        access_token = create_access_token(identity=username)
        set_access_cookies(response, access_token)
        return response
    else:
        return jsonify({'message': 'login','status': '1'})


# DELETE
@db_api.route('/login', methods=['DELETE'])
def logout():
    response = jsonify({'message': 'logout','status': '0'})
    response.set_cookie('access_token_cookie', '', expires=0)
    return response