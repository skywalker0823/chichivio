from flask import Blueprint,jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
import os,dotenv
import boto3
from database.models import Message,db

dotenv.load_dotenv()

board_api = Blueprint('board', __name__, url_prefix='/api/board')

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
    print("page:",page)
    # 目前抓取全部留言 -> 回傳
    try:
        messages = Message.query.all()
        print("-->",messages)
        if messages:
            messages_list = []
            for message in messages:
                messages_list.append({
                    'id': message.id,
                    'user_name': message.user_name,
                    'title': message.title,
                    'content': message.content,
                    'timestamp': message.timestamp,
                    'image_id': message.image_id
                })
            return jsonify({'message': 'get_board','status': '0','messages': messages_list})
        else:
            print("error1, message is empty")
            return jsonify({'message': 'get_board','status': '1'})
    except Exception as e:
        print(e)
        print("error2")
        return jsonify({'message': 'get_board','status': '1'})


# Post 主要功能OK
@board_api.route('/', methods=['POST'])
@jwt_required()
def post_board():
    data = request.get_json()
    #取的使用者id
    username = get_jwt_identity()
    message = {
        'title': data['title'],
        'content': data['content'],
        'time': data['time']
    }
    try:
        new_message = Message(title = message['title'], content = message['content'], user_name = username, timestamp = message['time'])
        db.session.add(new_message)
        db.session.commit()
        new_message_id = new_message.id
        #請送回ID
        return jsonify({'message': 'post_board','status': '0','id': new_message_id})
    except Exception as e:
        print(e)
        return jsonify({'message': 'post_board','status': '1'})


@board_api.route('/', methods=['DELETE'])
@jwt_required()
def delete_board():
    print("delete_board hit!")
    comment_id = request.args.get('comment_id')
    print(comment_id)
    result = db.get_or_404(Message, comment_id)
    if result:
        db.session.delete(result)
        db.session.commit()
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

