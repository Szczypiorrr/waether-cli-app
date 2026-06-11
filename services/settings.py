import json
from services.validator import validate_days, validate_city

def load_default_city():
    try:
        with open("data/settings.json", "r") as f:
            data = json.load(f)
            default_city = data["default_city"]

            return default_city
    except FileNotFoundError:
        return None
    
def load_default_days():
    try:
        with open("data/settings.json", "r") as f:
            data = json.load(f)
            default_days = data["days"]

            return default_days
    except FileNotFoundError:
        return None

def save_default_city(city):
    if not validate_city(city):
        return
    
    try:
        with open("data/settings.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return None

    data["default_city"] = city

    with open("data/settings.json", "w") as f:
        json.dump(data, f, indent=4)


def save_default_days(days):
    if not validate_days(days):
        return
    
    try:
        with open("data/settings.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return None
        
    data["days"] = days

    with open("data/settings.json", "w") as f:
        json.dump(data, f, indent=4)