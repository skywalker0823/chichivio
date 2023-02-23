# Create mysql database and table

from pymysql import connect, err, sys, cursors
import dotenv
import os

dotenv.load_dotenv()


conn = connect(
    host=os.environ['DB_HOST'],
    port=int(os.environ['DB_PORT']),
    database=os.environ['DB_DATABASE'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    charset='utf8mb4',
    cursorclass=cursors.DictCursor
)

cursor = conn.cursor()

# Create database
cursor.execute('CREATE DATABASE IF NOT EXISTS chi_vio;')