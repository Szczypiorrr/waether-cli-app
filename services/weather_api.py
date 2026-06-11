import requests
from dotenv import load_dotenv
import os
from models.weather import Weather

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
        data = response.json()

        weather = Weather(data["location"]["name"], data["current"]["temp_c"], data["current"]["condition"]["text"])
        return weather
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
