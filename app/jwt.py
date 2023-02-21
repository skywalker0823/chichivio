from flask import Blueprint,jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

jwt_api = Blueprint('jwt', __name__, url_prefix='/api/jwt')



