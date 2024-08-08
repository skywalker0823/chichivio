import dotenv
import requests
import os
import random
from modules.geo_code_check import check_place_by_geocode

dotenv.load_dotenv()

API_KEY = os.getenv("GOOGLE_MAP_API_KEY")


# 由於是透過經緯度找"附近50公里內景點" 因此 經緯度提供的地址查詢有很大的機會不會是景點地址，好在圖片本身會回帶地址資訊 也可省去一個 api 請求
# 接著要做的就是做可以針對圖片回傳資訊做篩出縣市區即可!
# maps api and places api

# 試著取得都市城鎮經緯度表

# 目前邏輯 User request -> 生成台灣隨機座標 -> 使用 place api 透過座標來傳回附近大量"景點" -> 景點中會有 photo_reference 並用他再次請求 place api 來找到該張圖片連結
# 整個過程若順利 需要存取兩次 place API, 前端目前是搭配免費的 embed api(測試調整成街景看看)
# 此方法比較像是景點認識測驗 而非 geo guess

# 第二方式 使用前端 embed api street view (此方法是免費的 只要克服前端UI顯示地點 就會很方便)
# 經緯度列表需要做大量測試
# 這個方法就類似自己開google map 給人看

# 第三方式 static street view 此方法會透過api 取得圖片 且該圖片無法互動 角度不可控可能影響體驗 除非一一篩檢 否則很難去避免視角差這件事
# Static street view : https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&heading=151.78&pitch=-0.76&key=YOUR_API_KEY&signature=YOUR_SIGNATURE

# 第四方式 street view metadata?

def get_random_taiwan_coords():
    #本島經緯度區間
    latitude = random.uniform(21.9, 25.3)
    longitude = random.uniform(120.0, 122.0)
    print(latitude, longitude)
    return latitude, longitude

def find_random_place(lat, lon):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lon}",
        "radius": 25000,  # 25公里
        "type": "tourist_attraction",  # 景點
        "key": API_KEY
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        results = response.json().get('results', [])
        if results:
            # random place
            place = random.choice(results)
            return place
    return None

def get_place_photo(photo_reference):
    # https://developers.google.com/maps/documentation/places/web-service/photos?hl=zh-tw
    url = f"https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "maxwidth": 1080,
        "photoreference": photo_reference,
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.url
    return None



def fetcher():
    # random tw coordinates
    lat, lon = get_random_taiwan_coords()
    place = find_random_place(lat, lon)
    if place and 'photos' in place:
        photo_reference = place['photos'][0]['photo_reference']
        photo_url = get_place_photo(photo_reference)
        location = place["plus_code"]["compound_code"]
        name = place["name"]
        place_id = place["place_id"]
        ans = check_place_by_geocode(location)
        return {'photo_reference': photo_reference, 'photo_url': photo_url, 'ans': ans, 'name': name, 'place_id':place_id}
    else:
        print("No photo available for this place.")