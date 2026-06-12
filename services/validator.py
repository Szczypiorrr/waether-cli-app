import re

def validate_city(city):
    """
    Checks if city name is valid (not empty and only letters/spaces).
    """
    city = city.strip()

    if not city:
        return False
    
    pattern = r"^[A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż -]+$"
    
    if not re.match(pattern, city):
        return False
    
    return True

def validate_menu_option(option, max_number):
    """
    Validates if menu option is within allowed range.
    """
    if not option:
        return False
    
    if not 0 < option <= max_number:
        return False
    
    return True


def validate_days(days):
    """
    Validates number of forecast days (1–14 range).
    """
    if not days:
        return False

    if not 0 < days <= 14:
        return False
    
    return True