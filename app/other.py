from flask import Blueprint,jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

other_api = Blueprint('other', __name__, url_prefix='/api/other')

# GET
@other_api.route('/', methods=['GET'])
def get_jwt():
    print("db_test hit!")
    # # request to firestore
    # db = firestore.Client()
    # doc_ref = db.collection(u'users').document(u'alice')
    # doc = doc_ref.get()
    # if doc.exists:
    #     print(u'Document data: {}'.format(doc.to_dict()))
    # else:
    #     print(u'No such document!')
    return jsonify({'message': 'db_test_ok','status': '0'})

