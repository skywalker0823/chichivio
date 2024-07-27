from flask import Blueprint,jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from database import dynamoDB
import os,dotenv
import boto3

dotenv.load_dotenv()

board_api = Blueprint('board', __name__, url_prefix='/api/board')

board_db = dynamoDB.DynamoDB_board()

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID_S3'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY_S3')
)

BUCKET_NAME = 'pikxl-main'

# client = MongoClient(os.getenv('DB_CONNECTION_DATA'))

# messages_db = client["chi_vio_db"]["messages"]

@board_api.route('/', methods=['GET'])
@jwt_required()
def get_board():
    print("get_board hit!")
    page = request.args.get('page')
    print(page)
    # 目前抓取全部留言 -> 回傳
    try:
        messages = board_db.get_board()
        if messages:
            return jsonify({'message': 'get_board','status': '0','messages': messages})
        else:
            print("error1")
            return jsonify({'message': 'get_board','status': '1'})
    except Exception as e:
        print(e)
        print("error2")
        return jsonify({'message': 'get_board','status': '1'})
        
        # messages_list = []
        # for message in messages:
        #     message['_id'] = str(message['_id'])
        #     messages_list.append(message)
        # print(messages_list)
        # return jsonify({'message': 'get_board','status': '0','messages': messages_list})

    except Exception as e:
        print(e)
        return jsonify({'message': 'get_board','status': '1'})


# Post 主要功能OK
@board_api.route('/', methods=['POST'])
@jwt_required()
def post_board():
    data = request.get_json()
    #取的使用者id
    user_id = get_jwt_identity()
    print(user_id)
    message = {
        'title': data['title'],
        'text': data['text'],
        # 'time': data['time'],
    }
    try:
        result = board_db.post_board(message['title'], message['text'])
        print(result)
        if result:
            return jsonify({'message': 'post_board','status': '0'})
        else:
            return jsonify({'message': 'post_board_db','status': '1'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'post_board','status': '1'})


@board_api.route('/', methods=['DELETE'])
@jwt_required()
def delete_board():
    print("delete_board hit!")
    comment_id = request.args.get('comment_id')
    print(comment_id)
    result = board_db.delete_board(comment_id)
    if result:
        return jsonify({'message': 'delete_board','status': '0'})
    else:
        return jsonify({'message': 'delete_board_db','status': '1'})
    
@board_api.route('/upload', methods=['POST'])
def upload_board():

    if 'file' not in request.files:
        print("no file part")
        return jsonify(success=False, message='No file part')
    else:
        file = request.files['file']
        if file.filename == '':
            return jsonify(success=False, message='No selected file')
        else:
            try:
                # test S3 authication
                response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, MaxKeys=1)
                print(response)
                return jsonify(success=True,message = "OK")
                
                # Celery should use here to upload images
                # file.save(f"tmp/{file.filename}")
                # file.save(file.filename)
                # print("上傳中...")
                # try:
                #     response = s3_client.upload_file(
                #         Bucket=BUCKET_NAME,Filename=file.filename,Key=file.filename,
                #     )
                # except Exception as e:
                #     print("u[load failed...")
                #     print(e)
                #     print(response)
                #     return jsonify(success=False, message='File could not be uploaded to S3')
                # finally:
                #     os.remove(f"tmp/{file.filename}")
                # print("上傳成功...")
                # return jsonify(success=True, message='File uploaded successfully')
            except Exception as e:
                print("上傳錯誤")
                print(e)
                return jsonify(success=False, message=str(e))

