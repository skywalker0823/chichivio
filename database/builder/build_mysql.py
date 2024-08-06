import pymysql
import os
from dotenv import load_dotenv

# Pure SQL Done then ORM.
# devide by prd and local

class Builder:
    load_dotenv()
    def __init__(self):
        self.conn = pymysql.connect(charset='utf8', host=os.getenv("DB"),
                                   password=os.getenv("DB_PASSWORD"), port=3306, user='root')
        self.cursor = self.conn.cursor()
        

    def start_initialize(self):
        self.cursor.execute("DROP DATABASE IF EXISTS pikxl")
        self.cursor.execute("CREATE DATABASE pikxl")
        self.cursor.execute("USE pikxl")
        self.conn.commit()

    def build_member(self):
        sql = """
            CREATE TABLE member (
                member_id INT AUTO_INCREMENT PRIMARY KEY,
                account VARCHAR(20) UNIQUE NOT NULL,
                password VARCHAR(20) NOT NULL
            )
        """
        self.cursor.execute(sql)
        self.conn.commit()


    def finallize(self):
        self.cursor.close()
        self.conn.close()




if __name__ == "__main__":
    load_dotenv()
    builder = Builder()
    builder.start_initialize()
    print("databases connected, start building tables...")
    builder.build_member()
    print("OK")
    builder.finallize()