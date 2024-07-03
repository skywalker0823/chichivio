import boto3
import os
import dotenv

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

