import requests

API_KEY = "your_api_key_here"
URL = "https://api.openweathermap.org/data/2.5/weather"

# Step 1: take location from the user
city = input("Enter city name: ")

# Step 2: call the Open Weather API
params = {"q": city, "appid": API_KEY, "units": "metric"}
try:
    response = requests.get(URL, params=params, timeout=10)
except requests.exceptions.RequestException:
    print("No internet connection!")
    raise SystemExit

data = response.json()

# Step 3: print basic weather data
if response.status_code == 200:
    print("----- Weather Report -----")
    print("City        :", data["name"], ",", data["sys"]["country"])
    print("Temperature :", data["main"]["temp"], "°C")
    print("Feels like  :", data["main"]["feels_like"], "°C")
    print("Humidity    :", data["main"]["humidity"], "%")
    print("Condition   :", data["weather"][0]["description"])
    print("Wind speed  :", data["wind"]["speed"], "m/s")
else:
    print("Error:", data.get("message"))
