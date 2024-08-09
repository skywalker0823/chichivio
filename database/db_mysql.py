import pymysql
import os
import dotenv
from dbutils.pooled_db import PooledDB

dotenv.load_dotenv()

hosts = [os.getenv('DB')]


# 請先看mysql 官方文件! https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html


def get_connection():
        for host in hosts:
            print(host)
        POOL = PooledDB(
            creator=pymysql,
            maxconnections=3,
            mincached=1,
            blocking=True,
            ping=0,
            host=host,
            port=3306,
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database = 'pikxl',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        connection = POOL.connection()
        return connection

connection = get_connection()

class User:
    def get_user_info(self, account):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM member WHERE account = %s"
            cursor.execute(sql, (account,))
            user_info = cursor.fetchone()
            return user_info
    
    def update_user_info(self, member_id, data):
         with connection.cursor() as cursor:
             sql = "UPDATE member SET %s = %s WHERE member_id = %s"
             updates = ', '.join([f"{key} = %s" for key in data])
             cursor.execute(sql % (updates, member_id) + tuple(data.values()))
             connection.commit()
             return cursor.rowcount
    
    def insert_user_info(self, data):
        with connection.cursor() as cursor:
            keys = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            sql = f"INSERT INTO member ({keys}) VALUES ({placeholders})"
            cursor.execute(sql, tuple(data.values()))
            connection.commit()
            return cursor.lastrowid

    
class Comments:
     def get_comments(self, post_id):
        pass

class Geo:
    def get_geo_score(self, member_id):
        pass

    def update_geo_score(self, member_id, data):
        pass