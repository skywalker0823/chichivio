# from app import redis_db
from redis import Redis
import os

redis_db = Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'))

def hello():
    redis_db.incr('hits')
    counter = str(redis_db.get('hits'),'utf-8')
    return counter
