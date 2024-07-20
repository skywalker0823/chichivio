from flask import Blueprint
from flask import jsonify, request
from flask_socketio import emit, join_room, leave_room
from . import SocketIO

chat_api = Blueprint('chat', __name__)


socketio = SocketIO

# @socketio.on('message')
# def handle_message(msg):
#     print(f"Received message{msg}")
#     emit('message', msg, broadcast=True)

