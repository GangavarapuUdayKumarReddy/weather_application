from django.urls import path
from .views import weather_view,saved_weather_data_view

urlpatterns = [
    path('', weather_view, name='weather_view'),  
    path('saved/',saved_weather_data_view, name='saved_weather'),
]
