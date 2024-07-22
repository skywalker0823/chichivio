import boto3
import os
import dotenv

dotenv.load_dotenv()

dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv('AWS_REGION'),

    # 僅供Local 測試使用 正式環境不需要
    # aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    # aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

dynamo_table_user = dynamodb.Table(os.getenv('DYNAMO_TABLE'))
dynamo_table_board = dynamodb.Table(os.getenv('DYNAMO_TABLE_BOARD'))