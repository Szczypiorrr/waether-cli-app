from services.settings import load_default_city, save_default_city, load_default_days, save_default_days
from services.weather_api import get_current_weather, get_weather_forecast
import time
from services.validator import validate_menu_option, validate_city, validate_days

def error_and_return(message, delay=3):
    print(message)
    time.sleep(delay)
    generate_menu()

def wait_and_return(delay=5):
    time.sleep(delay)
    generate_menu()

def wait_and_return_settings(delay=3):
    time.sleep(delay)
    settings_menu()

def print_header():
    print("=================================")
    print("        WEATHER CLI APP")
    print("=================================\n")

def print_default_weather():
    default_city = load_default_city()
    if default_city is None:
        print("Failed to load default city, using 'Warsaw'")
        default_city = "Warsaw"

    print(f"Default city: {default_city}\n")
    print("Current weather:")

    default_weather = get_current_weather(default_city)
    print(f"Temperature: {default_weather.temperature}°C")
    print(f"Condition: {default_weather.condition}")

def settings_menu():
        print("\nSELECT OPTION")
        print("1. Set default city")
        print("2. Set default forecast days")
        print("3. Return to main menu")

        try:
            selected_option = int(input("Enter selected number: "))
        except ValueError:
            error_and_return("Invalid type of data, must be a number.")
        except:
            error_and_return("An unexpected error occurred")

        if not validate_menu_option(selected_option, 3):
            error_and_return("The number must be between 1-3")

        if selected_option == 1:
            city = input("Enter name of city you want to set as default: ")
            if not validate_city(city):
                error_and_return("Invalid entered city")

            save_default_city(city)
            
            print("Default city has been changed succesfully")

            wait_and_return_settings()

        if selected_option == 2:
            days = int(input("Enter the number of days you want to set as default: "))
            
            if not validate_days(days):
                error_and_return("Invalid number of days, must be between 1-14")

            save_default_days(days)
            
            print("Default number of days has been changed succesfully")

            wait_and_return_settings()

        if selected_option == 3:
            generate_menu()

def generate_menu():
    print_header()
    print_default_weather()
    
    print("\n=================================")
    print("              MENU")
    print("=================================")
    print("SELECT OPTION")
    print("1. Show current weather (by city)")
    print("2. Show weather forecast (by city + days)")
    print("3. Show default weather forecast")
    print("4. Settings")
    print("5. Exit")

    try:
        selected_option = int(input("Enter selected number: "))
    except ValueError:
        error_and_return("Invalid type of data, must be a number.")
    except:
        error_and_return("An unexpected error occurred")

    if not validate_menu_option(selected_option, 5):
        error_and_return("The number must be between 1-5")

    if selected_option == 1:
        city = input("Enter city: ")

        if not validate_city(city):
            error_and_return("Invalid entered city")

        weather = get_current_weather(city)

        if not weather:
            error_and_return("An error occurred while fetching weather data.")

        print(f"Temperature: {weather.temperature}°C")
        print(f"Condition: {weather.condition}")

        wait_and_return()

    elif selected_option == 2:
        city = input("Enter city: ")

        if not validate_city(city):
            error_and_return("Invalid entered city")

        days = int(input("Enter the number of days: "))

        if not validate_days(days):
            error_and_return("Invalid number of days, must be between 1-14")

        weather = get_weather_forecast(city, days)

        if not weather:
            error_and_return("An error occurred while fetching weather data.")

        print(f"\n{days}-day weather forecast for {city}:\n")
        for day in weather:
            print(f"{day["date"]}: {day["temp"]}°C {day["condition"]}")

        wait_and_return()

    elif selected_option == 3:
        default_city = load_default_city()
        if default_city is None:
            print("Failed to load default city, using 'Warsaw'")
            default_city = "Warsaw"

        default_days = load_default_days()

        if default_days is None:
            print("Failed to load default number of days, using 7")
            default_days = 7

        weather = get_weather_forecast(default_city, default_days)

        if weather:
            print(f"\n{default_days}-day weather forecast for {default_city}:\n")
            for day in weather:
                print(f"{day["date"]}: {day["temp"]}°C {day["condition"]}")

        wait_and_return()

    elif selected_option == 4:
        settings_menu()

    elif selected_option == 5:
        print("Thank you for using our weather application, we hope you liked it!")
        return


generate_menu()