import dotenv
import requests
import os

dotenv.load_dotenv()

API_KEY = os.getenv("GOOGLE_MAP_API_KEY")


def check_place_by_geocode(compound_code):
    url = f"https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": compound_code,
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get('results', [])
        if results:
            address_components = results[0].get('address_components', [])
            for component in address_components:
                if 'administrative_area_level_1' in component.get('types', []):
                    return component.get('long_name')
    return None