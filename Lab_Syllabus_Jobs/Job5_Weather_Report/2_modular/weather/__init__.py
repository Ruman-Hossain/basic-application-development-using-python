"""weather package: get current weather from the OpenWeather API and show it."""

from .api import get_weather
from .display import print_report

__all__ = ["get_weather", "print_report"]
