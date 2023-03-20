from flask import Flask, render_template
from flask_socketio import SocketIO, emit




# socketio = SocketIO(app)


@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('send_message')
def handle_send_message(data):
    print(f"{data['name']}: {data['text']}")
    emit('receive_message', data, broadcast=True)

