
from flask import Blueprint, jsonify, request
from modules import stock_

stock_api = Blueprint('stock_api', __name__, url_prefix='/api/stock')

@stock_api.route('/', methods=['GET'])
def stock():
    stock = request.args.get('stock')
    print(stock,"stock hit!")
    try:
        result = stock_.get_stock_data(stock)
        if result['status'] == '0':
            return jsonify({'message': 'stock','status': '0','data': result['data']})
        else:
            return jsonify({'message': 'stock','status': '1'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'stock','status': '1'})