from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

class DB:
    def __init__(self) -> None:
        ssl_ca_paths = ["/etc/ssl/certs/ca-certificates.crt", "/etc/ssl/cert.pem"]
        ssl_ca = None
        for path in ssl_ca_paths:
            if os.path.exists(path):
                ssl_ca = path
                break
        self.connection = pymysql.connect(
            host = os.getenv("HOST"),
            user = os.getenv("USERNAME"),
            password = os.getenv("PASSWORD"),
            database = os.getenv("DATABASE"),
            ssl_ca = ssl_ca
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