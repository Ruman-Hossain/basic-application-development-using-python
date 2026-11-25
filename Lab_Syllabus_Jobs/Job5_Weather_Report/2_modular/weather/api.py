import requests

from .config import API_KEY, URL


def get_weather(city):
    """Ask the API for a city's weather. Returns (status_code, data_dictionary)."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(URL, params=params, timeout=10)
    return response.status_code, response.json()
