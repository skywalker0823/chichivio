from flask import Blueprint,jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, set_access_cookies, get_jwt_identity, verify_jwt_in_request
from database.models import User,db

login_api = Blueprint('login', __name__, url_prefix='/api/login')

@login_api.route('/', methods=['GET'])
def check_login():
    verify_jwt_in_request()
    username = get_jwt_identity()
    if username:
        return jsonify({'message': 'check_login','status': '0','username': username})
    else:
        return jsonify({'message': 'check_login','status': '1'})

# POST
@login_api.route('/', methods=['POST'])
def login():
    print(request.json,"login hit!")
    username = request.json['username']
    password = request.json['password']
    print(username,password)
    try:
        user = User.query.filter_by(username=username).first()
        print(user)
        print(user.username,user.password)
        if user and user.password == password:
            print("user get, login OK")
            response = jsonify({'message': 'login','status': "0"})
            access_token = create_access_token(identity=username)
            set_access_cookies(response, access_token)
            return response
        else:
            print("wrong user or password")
            return jsonify({'message': 'login','status': '1'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'db_test','status': '1'})

# DELETE
@login_api.route('/', methods=['DELETE'])
def logout():
    print("user logout!")
    response = jsonify({'message': 'logout','status': '0'})
    response.set_cookie('access_token_cookie', '', expires=0)
    return response

