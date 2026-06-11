import requests
from dotenv import load_dotenv
import os

load_dotenv()

base_url = "http://api.weatherapi.com/v1"
API_KEY = os.getenv('WEATHER_API_KEY')

def get_current_weather(city):
    url = f"{base_url}/current.json"

    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

