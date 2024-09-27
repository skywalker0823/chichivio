# from app import redis_db
from redis import Redis
import os
import json

redis_db = Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'))

def hello():
    redis_db.incr('hits')
    counter = str(redis_db.get('hits'),'utf-8')
    return counter

def add_message(message):
    print(message)
    redis_db.rpush('messages', json.dumps(message))
    redis_db.ltrim('messages',0,99)
    return {'message': message,'status': 0}

def get_all_messages():
    messages = redis_db.lrange('messages',0,-1)
    decoded_messages = [json.loads(message) for message in messages]
    return {'status':0,'message':decoded_messages}