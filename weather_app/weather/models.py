from django.db import models

class CityWeather(models.Model):
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField()
    searched_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.city_name} - {self.temperature}°C"