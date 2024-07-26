from django.shortcuts import render
import os, math

import requests

def get_Data(city_name):
    api_key = os.environ['api_key']

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(url).json()

    if response['cod'] == 200:
        return response
    else:
        return "error"

def weather(request):
    
    if request.method == 'POST':
        city = request.POST['city']
        
        data = get_Data(city)

        if data == 'error':
            return render(request, 'weather.html',{'erro':'Escreva uma cidade inválida'})

        for key, value in data['main'].items():
            if key == 'temp':
                aux = value - 273.15
                data['main'][key] = math.ceil(aux)

        data['main']['description'] = data['weather'][0]['description']
        data['main']['name'] = city

        return render(request, 'weather.html', {'data':data['main']})

    return render(request, "weather.html")


 