import json
from services.validator import validate_days, validate_city

def load_default_city():
    with open("data/settings.json", "r") as f:
        data = json.load(f)
        default_city = data["default_city"]

        return default_city
    
def load_default_days():
    with open("data/settings.json", "r") as f:
        data = json.load(f)
        default_days = data["days"]

        return default_days

def save_default_city(city):
    if not validate_city(city):
        return
    
    with open("data/settings.json", "r") as f:
        data = json.load(f)
        
    data["default_city"] = city

    with open("data/settings.json", "w") as f:
        json.dump(data, f, indent=4)


def save_default_days(days):
    if not validate_days(days):
        return
    
    with open("data/settings.json", "r") as f:
        data = json.load(f)
        
    data["days"] = days

    with open("data/settings.json", "w") as f:
        json.dump(data, f, indent=4)