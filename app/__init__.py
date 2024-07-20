# static website, flask app, personal website, huichi
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, current_user, get_jwt_identity, create_access_token, set_access_cookies
from datetime import datetime
from datetime import timedelta
from pathlib import Path
import secrets
from dotenv import load_dotenv
import os
from database import planet_scale, mongo, dynamoDB
from flask_socketio import SocketIO



def create_app():
    # 建立Flask物件, 並設定靜態檔案與模板檔案的路徑
    # 使用Path物件, 並使用parent屬性, 可以往上一層目錄
    app = Flask(__name__, static_url_path='/',
                static_folder = Path(__file__).parent.parent / 'static',
                template_folder = Path(__file__).parent.parent / 'templates')
    
    load_dotenv()

    # 設定JWT的secret key,should change to environment for env
    # app.config['JWT_SECRET_KEY'] = secrets.token_hex(16)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # 將JWT存在cookies中
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']

    # 設置JWT過期時間
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)

    jwt = JWTManager(app)

    CORS(app)

    socketio = SocketIO(app, async_mode='gevent', cors_allowed_origins="*")

    from app.login import login_api
    from app.other import other_api
    from app.member import member_api
    from app.board import board_api
    from app.signup import signup_api
    from app.stock import stock_api
    from app.apod import apod_api
    from app.chat import chat_api

    app.register_blueprint(login_api)
    app.register_blueprint(other_api)
    app.register_blueprint(member_api)
    app.register_blueprint(board_api)
    app.register_blueprint(signup_api)
    app.register_blueprint(stock_api)
    app.register_blueprint(apod_api)
    app.register_blueprint(chat_api)

    #確認用
    @socketio.on('system')
    def handle_message(data):
        print('Message received: ' + data['data'])
        socketio.emit('system-response', {'data': 'Response from server: '+ data['data']})

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

    @app.route('/stock', methods=['GET'])
    @jwt_required()
    def stock():
        return render_template('stock.html')

    @app.route('/apod', methods=['GET'])
    def apod():
        return render_template('apod.html')


    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        print("trigger unauthorized_response")
        response = make_response(jsonify({'msg': 'Unauthorized'}), 401)
        return redirect('/')
    
    @jwt.token_verification_failed_loader
    def token_verification_failed_response(callback):
        print("trigger token_verification_failed_response")
        response = make_response(jsonify({'msg': 'Token verification failed'}), 401)
        return render_template('index.html', response=response)

    # print("MongoDB is connected" if mongo.Mongo().is_connected() else "MongoDB FAILED to connect")
    # print("PlanetScaleDB is connected" if planet_scale.DB().is_connected() else "PlanetScaleDB FAILED to connect")
    print("DynamoDB is connected" if dynamoDB.DynamoDB().is_connected() else "DynamoDB FAILED to connect")

    return app, socketio