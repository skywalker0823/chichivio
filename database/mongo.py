from pymongo import MongoClient
import os, dotenv

dotenv.load_dotenv()

class Mongo:
    def __init__(self) -> None:
        self.client = MongoClient(os.getenv('DB_CONNECTION_DATA'))

    def get_user(self, username, password):
        query = {"username": username,"password": password}
        result = self.client["chi_vio_db"]["users"].find_one(query)
        return result

    def insert_user(self, username, password):
        query = {"username": username,"password": password}
        result = self.client["chi_vio_db"]["users"].insert_one(query)
        return result        
        