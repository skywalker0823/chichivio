import boto3
import os
import dotenv
import datetime

dotenv.load_dotenv()

class DynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name=os.getenv('AWS_REGION'),

            # 僅供Local 測試使用 正式環境不需要
            # aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            # aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        self.table = self.dynamodb.Table(os.getenv('DYNAMO_TABLE'))

    def is_connected(self):
        try:
            self.table.scan(Limit=1)
            return True
        except Exception as e:
            print("Exception occurred: {}".format(e))
            return False

    def get_user(self, username, password):
        try:
            print("DB trying to get user...")
            response = self.table.get_item(
                Key={
                    'id': username                }
            )
            return response.get('Item', None)
        except Exception as e:
            print("DB get user failed, Exception occurred: {}".format(e))
            return None

    def insert_user(self, username, password):
        try:
            print("DBtrying to insert user...")
            response = self.table.put_item(
                Item={
                    'id': username,
                    'password': password
                }
            )
            return response
        except Exception as e:
            print("DB insert user failed, Exception occurred: {}".format(e))
            return None


class DynamoDB_board(DynamoDB):
    def __init__(self):
        super().__init__()
        self.table = self.dynamodb.Table(os.getenv('DYNAMO_TABLE_BOARD'))

    def get_board(self):
        try:
            print("DB trying to get board...")
            response = self.table.scan()
            print(response)
            items = response['Items']
            print("items:",items) 
            return items
        except Exception as e:
            return None

    def post_board(self, title, text): 
        try:
            response = self.table.put_item(
                Item={
                    #預計 id 組成: user_id+timestamp
                    'comment_id': datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
                    'title': title,
                    'text': text
                    # 'time': time
                }
            )
            return response  # Return the DynamoDB response for potential further processing
        except Exception as e:
            # Handle errors (e.g., log the error, return an error status)
            print(f"Error posting to board: {e}")
            return None
        
    def delete_board(self, comment_id):
        try:
            response = self.table.delete_item(
                Key={
                    'comment_id': comment_id
                }
            )
            return response  # Return the DynamoDB response for potential further processing
        except Exception as e:
            # Handle errors (e.g., log the error, return an error status)
            print(f"Error deleting from board: {e}")
            return None