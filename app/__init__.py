# static website, flask app, personal website, huichi
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, current_user, get_jwt_identity, create_access_token, set_access_cookies
from datetime import datetime
from datetime import timedelta
from pathlib import Path
import secrets
from database import planet_scale, mongo



def create_app():
    # 建立Flask物件, 並設定靜態檔案與模板檔案的路徑
    # 使用Path物件, 並使用parent屬性, 可以往上一層目錄
    app = Flask(__name__, static_url_path='/',
                static_folder = Path(__file__).parent.parent / 'static',
                template_folder = Path(__file__).parent.parent / 'templates')

    # firebase_admin initialize
    # cred = credentials.Certificate('../keys/firebase-adminsdk.json')
    # initialize_app(cred)

    # 設定JWT的secret key
    app.config['JWT_SECRET_KEY'] = secrets.token_hex(16)

    # 將JWT存在cookies中
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']

    # 設置JWT過期時間
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

    jwt = JWTManager(app)

    CORS(app)

    from app.login import login_api
    from app.other import other_api
    from app.member import member_api
    from app.board import board_api
    from app.signup import signup_api

    app.register_blueprint(login_api)
    app.register_blueprint(other_api)
    app.register_blueprint(member_api)
    app.register_blueprint(board_api)
    app.register_blueprint(signup_api)


    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/about', methods=['GET'])
    def about():
        return render_template('about.html')

    @app.route('/contact', methods=['GET'])
    def contact():
        return render_template('contact.html')
    
    @app.route('/member', methods=['GET'])
    @jwt_required()
    def member():
        return render_template('member.html')

    @app.route('/board', methods=['GET'])
    @jwt_required()
    def board():
        return render_template('board.html')

    @app.route('/chat', methods=['GET'])
    @jwt_required()
    def chat():
        return render_template('chat.html')


    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        response = make_response(jsonify({'msg': 'Unauthorized'}), 401)
        return response
        # return jsonify({"msg": "Not authorized"}), 401

    print("MongoDB is connected" if mongo.Mongo().is_connected() else "MongoDB FAILED to connect")
    # print("PlanetScaleDB is connected" if planet_scale.DB().is_connected() else "PlanetScaleDB FAILED to connect")
    
    return app