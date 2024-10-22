import requests

API_KEY = 'API_KEY'

def get_weather_data(city_name):
    url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city_name}&days=7&aqi=no&alerts=no'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None