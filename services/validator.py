import re

def validate_city(city):
    city = city.strip()

    if not city:
        return False
    
    pattern = r"^[A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż -]+$"
    
    if not re.match(pattern, city):
        return False
    
    return True

def validate_menu_option(option):
    if not option:
        return False
    
    if not 0 < option < 6:
        return False
    
    return True


def validate_days(days):
    if not days:
        return False

    if not 0 < days <= 14:
        return False
    
    return True