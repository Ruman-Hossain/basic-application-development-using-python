import requests

from weather import get_weather, print_report

if __name__ == "__main__":
    city = input("Enter city name: ")
    try:
        status, data = get_weather(city)
    except requests.exceptions.RequestException:
        print("No internet connection!")
        raise SystemExit

    if status == 200:
        print_report(data)
    else:
        print("Error:", data.get("message"))
