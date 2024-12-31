from database.models import db, NightMarkets
import json
from app import create_app

appe = create_app()

with appe.app_context():
    # 讀取 JSON 檔案
    with open('main.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 將資料插入資料庫
    for region, counties in data.items():
        for county, markets in counties.items():
            for market in markets:
                night_market = NightMarkets(
                    name=market['name'],
                    part=region,
                    county=county,
                    location=market['location'],
                    operating_days=market.get('operating_days', None)
                )
                db.session.add(night_market)

    # 提交變更
    db.session.commit()