import dotenv
import requests
import os
import random
import json

dotenv.load_dotenv()

API_KEY = os.getenv("GOOGLE_MAP_API_KEY")


# 由於是透過經緯度找"附近50公里內景點" 因此 經緯度提供的地址查詢有很大的機會不會是景點地址，好在圖片本身會回帶地址資訊 也可省去一個 api 請求
# 接著要做的就是做可以針對圖片回傳資訊做篩出縣市區即可!
# maps api and places api


# 新版 API



def tester():
    url = 'https://places.googleapis.com/v1/places:searchNearby'
    payload = {
        "includedTypes": ["restaurant"],
        "maxResultCount": 10,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": 37.7937,
                    "longitude": -122.3965
                },
                "radius": 500.0
            }
        }
    }

    headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': API_KEY,
            'X-Goog-FieldMask': 'places.displayName'
        }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Request successful.")
        print(response.json())
    else:
        print("Request failed.")
        print(f"Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    tester()
