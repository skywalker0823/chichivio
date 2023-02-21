# static website, flask app, personal website, huichi
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, current_user, get_jwt_identity
# import random generator for secret key
import secrets




def create_app():
    app = Flask(__name__, static_url_path='/', static_folder='../static', template_folder='../templates')

    # 設定JWT的secret key
    app.config['JWT_SECRET_KEY'] = secrets.token_hex(16)

    # 將JWT存在cookies中
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']

    jwt = JWTManager(app)
    
    CORS(app)

    from app.db import db_api
    from app.jwt import jwt_api

    app.register_blueprint(db_api)
    app.register_blueprint(jwt_api)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')
    
    @app.route('/member')
    @jwt_required()
    def member():
        return render_template('member.html')

    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        return jsonify({"msg": "Missing Authorization Header"}), 401


    return app