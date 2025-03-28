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
from database.db_redis import hello
from flask_migrate import Migrate

socketio = SocketIO()

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
    
    migrate = Migrate(app, db)
    
    socketio.init_app(app,async_mode='gevent', cors_allowed_origins="*")

    jwt = JWTManager(app)

    CORS(app)

    from app.login import login_api
    from app.member import member_api
    from app.board import board_api
    from app.signup import signup_api
    from app.geo import geo_api
    from app.chat import chat_api
    from app.county import county_api

    app.register_blueprint(login_api)
    app.register_blueprint(member_api)
    app.register_blueprint(board_api)
    app.register_blueprint(signup_api)
    app.register_blueprint(geo_api)
    app.register_blueprint(chat_api)
    app.register_blueprint(county_api)
        
    @app.route('/', methods=['GET'])
    def index():
        redis_response = hello()
        return render_template('index.html', count = redis_response)

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
    @jwt_required()
    def geo():
        return render_template('geo.html')
    
    @app.route('/foodprint', methods=['GET'])
    @jwt_required()
    def foodprint():
        return render_template('foodprint.html')
    
    @app.route('/foodprint/<county>', methods=['GET'])
    @jwt_required()
    def counties(county):
        print(county)
        return render_template('county.html', county=county)
    
    @app.route('/test', methods=['GET'])
    def test():
        return render_template('test.html')

    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        print("trigger unauthorized_response")
        # return make_response(jsonify({'msg': 'You Are Unauthorized.','status': 401}), 401)
        return redirect('https://http.cat/401')

    @jwt.token_verification_failed_loader
    def token_verification_failed_response(callback):
        print("trigger token_verification_failed_response")
        response = make_response(jsonify({'msg': 'Token verification failed'}), 401)
        return render_template('index.html', response=response)

    return app