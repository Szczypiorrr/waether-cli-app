# weather-cli-app
A simple Weather CLI application built in Python using external weather API.

The goal of this project is to demonstrate working with REST APIs, JSON data handling, CLI application design, input validation, configuration management, and modular project architecture.

## ⚙️ How to run

### 1. Clone repository
```bash
git clone https://github.com/Szczypiorrr/weather-cli-app.git
cd weather-cli-app
```
### 2. Create virtual environment
```bash
python -m venv venv
```
### 3. Activate virtual environment
Windows:
```bash
venv\Script\activate
```

Mac / Linux:
```bash
source venv/bin/activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. Add API key
Create .env file in root directory:
```bash
WEATHER_API_KEY=your_api_key_here
```
### 6. Run project
```bash
python main.py
```

## 📌 Features

- Get current weather for any city
- Get weather forecast for selected number of days
- Load default city from settings.json
- Load default forecast days from settings.json
- Save default city and forecast settings via CLI
- Validate user input (city, menu options, forecast days)
- Handle API errors and missing responses
- Modular architecture (services, models, validation layer)
- CLI-based user interaction system

## 🧱 Project structure
```text
weather-cli-app/
│
├── main.py # CLI application entry point
│
├── models/
│   └── weather.py # Weather data model
│
├── services/
│   ├── weather_api.py # API requests and data parsing
│   ├── settings.py # Load/save configuration (JSON)
│   └── validator.py # Input validation functions
│
├── data/
│   └── settings.json # Default city and forecast settings
│
├── reports/
│   └── (optional future reports/logs)
│
├── requirements.txt
│
├── .env # API key (not pushed to GitHub)
│
└── README.md
```

## 🚀 Technologies

- Python 3.12
- Git/GitHub
- REST API (requests libary)
- JSON file handling
- Environment variables (.env)
- CLI application design


## 📊 Example CLI output
```text
=================================
        WEATHER CLI APP
=================================

Default city: Warsaw
Current weather:
Temperature: 12°C
Condition: Cloudy

=================================
              MENU
=================================
1. Show current weather (by city)
2. Show weather forecast
3. Show default weather forecast
4. Settings
5. Exit
```

## 🧠 What I learned?

- Working with REST APIs and HTTP requests
- Parsing JSON responses into Python objects
- Managing configuration using JSON files
- Handling environment variables securely
- Building CLI applications
- Input validation and error handling
- Structuring medium-size Python projects
- Learning and applying DRY principle in Python projects

## 🔧 Possible improvements

- Add weather caching system (reduce API calls)
- Add hourly forecast support
- Add multiple saved cities (favorites system)
- Improve CLI UI (better formatting / colors)
- Add weather history tracking
- Export weather data to CSV or JSON reports

# 👤 Author

Created by Szczypiorrrr  
🔗 GitHub: https://github.com/Szczypiorrr