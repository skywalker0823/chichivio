from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, current_user, get_jwt_identity, create_access_token, set_access_cookies
from datetime import timedelta
from pathlib import Path
import secrets
from dotenv import load_dotenv
import os
from flask_socketio import SocketIO
from database.models import db

# Redis
# import redis
# redis_client = None

def create_app():
    app = Flask(__name__, static_url_path='/',
                static_folder = Path(__file__).parent.parent / 'static',
                template_folder = Path(__file__).parent.parent / 'templates')
    
    load_dotenv()

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)

    # SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()

    jwt = JWTManager(app)

    CORS(app)

    socketio = SocketIO(app, async_mode='gevent', cors_allowed_origins="*")

    from app.login import login_api
    from app.other import other_api
    from app.member import member_api
    from app.board import board_api
    from app.signup import signup_api
    from app.geo import geo_api
    from app.chat import chat_api

    app.register_blueprint(login_api)
    app.register_blueprint(other_api)
    app.register_blueprint(member_api)
    app.register_blueprint(board_api)
    app.register_blueprint(signup_api)
    app.register_blueprint(geo_api)
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

    @app.route('/geo', methods=['GET'])
    # @jwt_required()
    def geo():
        return render_template('geo.html')
    
    @app.route('/test', methods=['GET'])
    def test():
        return render_template('test.html')

    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        print("trigger unauthorized_response")
        return make_response(jsonify({'msg': 'You Are Unauthorized.','status': 401}), 401)

    @jwt.token_verification_failed_loader
    def token_verification_failed_response(callback):
        print("trigger token_verification_failed_response")
        response = make_response(jsonify({'msg': 'Token verification failed'}), 401)
        return render_template('index.html', response=response)

    # print("MongoDB is connected" if mongo.Mongo().is_connected() else "MongoDB FAILED to connect")
    # print("PlanetScaleDB is connected" if planet_scale.DB().is_connected() else "PlanetScaleDB FAILED to connect")
    # print("DynamoDB is connected" if dynamoDB.DynamoDB().is_connected() else "DynamoDB FAILED to connect")

    return app, socketio