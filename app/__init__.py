# static website, flask app, personal website, huichi
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager, jwt_required, current_user, get_jwt_identity, create_access_token, set_access_cookies
from datetime import datetime
from datetime import timedelta
import secrets

socketio = SocketIO()

def create_app():
    # 建立Flask物件, 並設定靜態檔案與模板檔案的路徑
    app = Flask(__name__, static_url_path='/', static_folder='../static', template_folder='../templates')

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

    app.register_blueprint(login_api)
    app.register_blueprint(other_api)
    app.register_blueprint(member_api)
    app.register_blueprint(board_api)


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

    # 個人頁面
    @app.route('/personal/<id>', methods=['GET'])
    @jwt_required()
    def board_detail(board_id):
        return render_template('board_detail.html')

    @app.route('/chat', methods=['GET'])
    def chat():
        return render_template('chat.html')


    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        # redirect to homepage
        # return redirect(url_for('index'))
        return jsonify({"msg": "Not authorized"}), 401
    
    return app