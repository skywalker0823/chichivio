# static website, flask app, personal website, huichi
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, current_user, get_jwt_identity
import secrets




def create_app():
    # 建立Flask物件, 並設定靜態檔案與模板檔案的路徑
    app = Flask(__name__, static_url_path='/', static_folder='../static', template_folder='../templates')

    # 設定JWT的secret key
    app.config['JWT_SECRET_KEY'] = secrets.token_hex(16)

    # 將JWT存在cookies中
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']


    jwt = JWTManager(app,)
    
    CORS(app)

    from app.login import login_api
    from app.other import other_api
    from app.member import member_api

    app.register_blueprint(login_api)
    app.register_blueprint(other_api)
    app.register_blueprint(member_api)

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

    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        return jsonify({"msg": "Not authorized"}), 401


    return app