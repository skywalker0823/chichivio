from flask import Blueprint,jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
import os,dotenv,json
import boto3
from werkzeug.utils import secure_filename
from database.models import Message,db
from datetime import datetime

# dotenv.load_dotenv()

board_api = Blueprint('board', __name__, url_prefix='/api/board')

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID_S3'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY_S3')
)

BUCKET_NAME = os.getenv('BUCKET_NAME')

@board_api.route('/', methods=['GET'])
@jwt_required()
def get_board():
    print("get_board hit!")
    page = int(request.args.get('page'))
    try:
        messages = Message.query.order_by(Message.timestamp.desc()).limit(5).offset((page-1)* 5 ).all()
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
            print(messages_list)
            return jsonify({'message': 'get_board','status': '0','messages': messages_list})
        else:
            print("error1, message is empty")
            return jsonify({'message': 'get_board','status': '1'})
    except Exception as e:
        print(e)
        print("error2")
        return jsonify({'message': 'get_board','status': '1'})

# Post 主要功能OK
# 單一請求 同時處理文字與圖片? 
# 給予文章與圖片同 id 就不需要把圖片id存SQL?
@board_api.route('/', methods=['POST'])
@jwt_required()
def post_board():
    #圖片檔案會是請求內的 'file' 變數
    file = request.files.get('file')
    data = request.form.get('data')
    data = json.loads(data)
    print(file,type(data))
    username = get_jwt_identity()
    message = {
        'title': data['title'],
        'content': data['content'],
        'time': data['time']
    }
    if not file:
        try:
            print("no file")
            new_message = Message(title = message['title'], content = message['content'], user_name = username, timestamp = message['time'])
            db.session.add(new_message)
            db.session.commit()
            new_message_id = new_message.id
            #請送回ID
            return jsonify({'message': 'post_board','status': '0','id': new_message_id,'image_id': None})
        except Exception as e:
            print(e)
            return jsonify({'message': 'post_board','status': '1'})
    else:
        try:
            print("file exists")
            now = datetime.now()
            stamp = now.strftime('%Y%m%d%H%M%S') + f'{now.microsecond}'
            img = request.files["file"]
            filename = secure_filename(img.filename)
            file_type = filename.split(".")[1]
            # 務必將檔案名稱入SQL db
            s3_client.put_object(
                Body=img,
                Bucket=BUCKET_NAME,
                Key=f"images/{stamp}_{filename}",
                ContentType=f"image/{file_type}"
            )
            
            new_message = Message(title = message['title'], content = message['content'], user_name = username, timestamp = message['time'], image_id = f'{stamp}_{filename}')
            db.session.add(new_message)
            db.session.commit()
            new_message_id = new_message.id
            print("upload_board success!")
            return jsonify({'message': 'upload_board','status': '0','id': new_message_id,'image_id':f'{stamp}_{filename}'})
        except Exception as e:
            print("error!",e)
            return jsonify({'message': 'upload_image_board','status': '1'})

# 文章刪除
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