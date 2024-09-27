from flask import Blueprint
from flask import jsonify, request
from flask_socketio import emit, join_room, leave_room
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from . import socketio
from database.db_redis import redis_db,add_message,get_all_messages
import json

chat_api = Blueprint('chat', __name__)

@socketio.on('messager_send')
def handle_message(data):
    verify_jwt_in_request()
    who = get_jwt_identity()
    print(f"""{who}:{data["msg"]}""")
    data["who"] = who
    data["type"] = "user"
    data["message"] = data["msg"]
    add_message(data)
    socketio.emit('messager_recieve', data)

@socketio.on('system')
def sys_confirm(data):
    verify_jwt_in_request()
    print('Message received: ' + data["data"])
    data["who"] = None
    all_messages = get_all_messages()
    data["message"] = all_messages["message"]
    data["type"] = "user"
    data["you"] = get_jwt_identity()
    sid = request.sid
    socketio.emit('system-response', data , room=sid)