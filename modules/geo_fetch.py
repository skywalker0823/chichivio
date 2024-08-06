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
            print(place)
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
        ans = check_place_by_geocode(location)
        return {'photo_reference': photo_reference, 'photo_url': photo_url, 'ans': ans, 'name': name}
    else:
        print("No photo available for this place.")