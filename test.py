import dotenv
import requests
import os


dotenv.load_dotenv()

API_KEY = os.getenv("GOOGLE_MAP_API_KEY")

# STATIC STREET VIEW
# 目前只需要打一次該API即可生成圖片與資訊 但前置較多(經緯度資料)


# places = [
#           [{ lat: 60.171001,  lng: 24.939350 },  {country: 'Finland'}],
#           [{ lat: 48.858093,  lng: 2.294694 },   {country: 'France'}],
#           [{ lat: 51.510020,  lng: -0.134730 },  {country: 'Great Britain'}],
#           [{ lat: 41.8902,    lng: 12.4922 },      {country: 'Italy'}],
#           [{ lat: 25.195302,  lng: 55.272879 },  {country: 'United Arab Emirates'}],
#           [{ lat: 1.283404,   lng: 103.863134 },  {country: 'Singapore'}],
#           [{ lat: 29.976768,  lng: 31.135538 },  {country: 'Egypt'}],
#           [{ lat: 40.757876,  lng: -73.985592 }, {country: 'United States'}]
#       ]

def tester():
    # 先取得台灣座標範圍 以此試著存取靜態圖片或街景
    # 以縣市 -> 區 如此來遊玩
    # 臺灣本島之地理位置為東經120°E至122°E、北緯22°N至25°N
    # >>> GEO coding API <<<
    #或換個方式 透過 景點-> 座標 -> 圖片 來遊玩?

    #改變 heading 來改變看的角度
    # 經緯度要加減多少才隨機得合理?
    # 動態街景是否會讓結果更好?
    response = requests.get(f"https://maps.googleapis.com/maps/api/streetview?size=600x300&location=60.171020,24.939350&heading=100.78&pitch=-0.76&key={API_KEY}")
    # response = requests.get(f"https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&heading=151.78&pitch=-0.76&key={API_KEY}&signature=YOUR_SIGNATURE")
    if response.status_code == 200:
        street_view_url = response.url
        print(f"Street view URL: {street_view_url}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    tester()


# 重要參考資料 
# https://www.letswrite.tw/d3-vue-taiwan-map/
# https://icelandcheng.medium.com/%E4%BD%BF%E7%94%A8google-map-api-geocoding-api-%E5%BE%97%E5%88%B0%E9%BB%9E%E4%BD%8D%E7%B8%A3%E5%B8%82%E9%84%89%E9%8E%AE%E8%B3%87%E6%96%99-25bf5f0e4a21
# https://developers.google.com/maps/documentation?hl=zh-tw