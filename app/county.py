# 假設 NightMarkets 已經在 database/models.py 中定義
from flask import Blueprint, jsonify, request
from database.models import NightMarkets, db

# 定義 Blueprint
county_api = Blueprint('county', __name__, url_prefix='/api/county')

# 回傳夜市資料的路由
@county_api.route('/', methods=['GET'])
def get_night_markets():
    print("get night markets")
    # 假設你希望根據縣市來查詢夜市資料
    county = request.args.get('county', default=None, type=str)  # 獲取 query string 參數 'county'
    print("county:"+ county)
    try:
        if county:
            # 若有傳入 county 參數，則查詢該縣市的夜市
            night_markets = NightMarkets.query.filter_by(county=county).all()
        else:
            # 若沒有傳入，則查詢所有夜市
            night_markets = NightMarkets.query.all()

        if night_markets:
            markets_list = []
            for market in night_markets:
                markets_list.append({
                    'id': market.id,
                    'name': market.name,
                    'county': market.county,
                    'location': market.location,
                    'operating_days': market.operating_days
                })
            print(markets_list)
            return jsonify({'message': 'get_night_markets', 'status': '0', 'night_markets': markets_list})
        else:
            return jsonify({'message': 'get_night_markets', 'status': '1', 'error': 'No night markets found'})

    except Exception as e:
        print("Error:", e)
        return jsonify({'message': 'get_night_markets', 'status': '1', 'error': str(e)})

