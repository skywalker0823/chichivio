from dotenv import load_dotenv
import os
import MySQLdb
import pymysql

load_dotenv()

class DB:
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host = os.getenv("HOST"),
            user = os.getenv("USERNAME"),
            password = os.getenv("PASSWORD"),
            database = os.getenv("DATABASE"),
            ssl_ca = "/etc/ssl/certs/ca-certificates.crt"
            # Mac OS ssl_ca
            # ssl_ca = "/etc/ssl/cert.pem"
        )
        self.cursor = self.connection.cursor()
    
    def is_connected(self):
        if self.connection.open:
            return True
        else:
            return False

    def get_user(self, username,password):
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username,password))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print("Exeception occured:{}".format(e))
            return None

    def insert_user(self, username, password):
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            return True
        except Exception as e:
            print("Exeception occured:{}".format(e))
            return False