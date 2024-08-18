from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, set_access_cookies, verify_jwt_in_request
import os, dotenv
from database.models import User,db

dotenv.load_dotenv()

signup_api = Blueprint('signin_api', __name__, url_prefix='/api/signup')

@signup_api.route('/', methods=['POST'])
def signup():
    print(request.json,"signup hit!")
    username = request.json['username']
    password = request.json['password']
    try:
        # result = database.get_user(username,password)
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print("user already exist, signin failed")
            return jsonify({'message': 'signin','status': '1'})
        
        new_user = User(username=username, password=password)
        print("trying to sign up...")
        db.session.add(new_user)
        db.session.commit()
        response = jsonify({'message': 'signup','status': "0"})
        access_token = create_access_token(identity=username)
        set_access_cookies(response, access_token)
        return response
    except Exception as e:
        print("signup error: ",e)
        return jsonify({'message': 'db_test','status': '1'})
