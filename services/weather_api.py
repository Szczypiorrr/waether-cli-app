import requests
from dotenv import load_dotenv
import os
from models.weather import Weather

load_dotenv()

base_url = "http://api.weatherapi.com/v1"
API_KEY = os.getenv('WEATHER_API_KEY')

def get_current_weather(city):
    """
    Fetches current weather data for a given city from WeatherAPI.
    Returns Weather object or None if request fails.
    """
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


def get_weather_forecast(city, days):
    """
    Fetches weather forecast for a given city and number of days.
    Returns list of dicts with date, temperature and condition.
    """
    url = f"{base_url}/forecast.json"

    params = {
        "key": API_KEY,
        "q": city,
        "days": days
    }    

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        forecast_days = data["forecast"]["forecastday"]

        result = []

        for day in forecast_days:
            date = day["date"]
            temp = day["day"]["avgtemp_c"]
            condition = day["day"]["condition"]["text"]

            result.append({
                "date": date,
                "temp": temp,
                "condition": condition
            })

        return result
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
