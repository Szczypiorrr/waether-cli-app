import json

def load_default_city():
    with open("data/settings.json", "r") as f:
        data = json.load(f)
        default_city = data["default_city"]

        return default_city
    
def save_default_city(city):
    with open("data/settings.json", "r") as f:
        data = json.load(f)
        
    data["default_city"] = city

    with open("data/settings.json", "w") as f:
        json.dump(data, f, indent=4)

