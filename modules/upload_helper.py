import os,dotenv
import boto3
from werkzeug.utils import secure_filename
import uuid

BUCKET_NAME = os.getenv("BUCKET_NAME")

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}


s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID_S3'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY_S3')
)

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"


def upload_file_to_s3(file, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        # in case the our s3 upload fails
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.filename}"}