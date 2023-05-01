from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3e6565ff7d92a4e489c65a3cebffc997'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    print(city_weather)

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {'weather' : weather} 

    cities = City.objects.all()

    form = CityForm()

    context = {'form' : form}

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() 

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) 

    context = {'weather_data' : weather_data}

    if request.method == 'POST': 
        form = CityForm(request.POST) 
        form.save()

 

 


    return render(request, 'weather/index.html', context) 