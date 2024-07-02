import boto3
import os
import dotenv

dotenv.load_dotenv()

class DynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name=os.getenv('AWS_REGION'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        self.table = self.dynamodb.Table(os.getenv('pikxl_dynamoDB'))

    def is_connected(self):
        try:
            self.table.scan(Limit=1)
            return True
        except Exception as e:
            print("Exception occurred: {}".format(e))
            return False

    def get_user(self, username, password):
        try:
            response = self.table.get_item(
                Key={
                    'username': username,
                    'password': password
                }
            )
            return response.get('Item', None)
        except Exception as e:
            print("Exception occurred: {}".format(e))
            return None

    def insert_user(self, username, password):
        try:
            response = self.table.put_item(
                Item={
                    'username': username,
                    'password': password
                }
            )
            return response
        except Exception as e:
            print("Exception occurred: {}".format(e))
            return None

