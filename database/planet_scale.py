from dotenv import load_dotenv
import os
import MySQLdb

load_dotenv()

class DB:
    def __init__(self) -> None:
        self.connection = MySQLdb.connect(
            host= os.getenv("HOST"),
            user=os.getenv("USERNAME"),
            passwd= os.getenv("PASSWORD"),
            db= os.getenv("DATABASE"),
            autocommit = True,
            ssl_mode = "VERIFY_IDENTITY",
            ssl      = {
                "ca": "/etc/ssl/cert.pem"
            }
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