from config import WEATHER_API_TOKEN
from pyowm.owm import OWM
from datetime import datetime


owm = OWM(WEATHER_API_TOKEN)
mgr = owm.weather_manager()

class Weather:
    def __init__(self, city, status, temperature, time, icon):
        self.city = city
        self.status = status
        self.temperature = temperature
        self.time = time
        self.icon = icon


def get_current_weather(city):
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temp_dict_kelvin = weather.temperature('celsius')
    time = datetime.fromtimestamp(weather.ref_time).strftime("%H:%M")
    return Weather(city=city, status=weather.status, temperature=int(temp_dict_kelvin['temp']), time=time, icon=weather.weather_icon_name + '.png')


def get_forecast(city, interval='3h', limit=9):
    observations = mgr.forecast_at_place(name=city, interval=interval, limit=limit)  # the observation object is a box containing a weather object
    forecast = []
    result = []
    for weather in observations.forecast:
        forecast.append(weather)
    for weather in forecast[::2]:
        temp_dict_kelvin = weather.temperature('celsius')
        time = datetime.fromtimestamp(weather.ref_time).strftime("%H:%M")
        result.append(Weather(city=city, status=weather.status, temperature=int(temp_dict_kelvin['temp']), time=time, icon=weather.weather_icon_name + '.png'))
    return result