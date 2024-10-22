from django.shortcuts import render
from .services import get_weather_data
from .models import CityWeather  
import datetime

def weather_view(request):
    city_name = request.GET.get('city', '')  
    data = None

    if city_name:
        data = get_weather_data(city_name)

    if data:
        today_weather = data['current']
        forecast = data['forecast']['forecastday']  
        CityWeather.objects.create(
            city_name=city_name,
            temperature=today_weather['temp_c']
        )

        hourly_forecast = forecast[0].get('hour', [])
        next_6_hours = hourly_forecast[:6] if len(hourly_forecast) >= 6 else hourly_forecast

        formatted_forecast = []
        for day in forecast:
            formatted_day = {
                'date': datetime.datetime.strptime(day['date'], '%Y-%m-%d').strftime('%A, %d %b %Y'),
                'avgtemp_c': day['day']['avgtemp_c'],
                'condition': day['day']['condition']['text'],
                'icon': day['day']['condition']['icon']
            }
            formatted_forecast.append(formatted_day)

        context = {
            'city': data['location']['name'],
            'today_weather': today_weather,
            'hourly_forecast': next_6_hours,  
            'forecast': formatted_forecast,  
        }
    else:
        context = {'error': 'Could not retrieve weather data'} if city_name else {}

    return render(request, 'weather/weather.html', context)


def saved_weather_data_view(request):
    saved_weather = CityWeather.objects.all().order_by('-searched_at')  
    context = {
        'saved_weather': saved_weather,
    }
    return render(request, 'weather/saved_weather.html', context)
