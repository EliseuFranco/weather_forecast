from django.shortcuts import render

import requests

def get_Data(city_name):
    api_key = '72decfa09a508b1c0ffeddfe426d5efe'
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
            return render(request, 'weather.html',{'erro':'Escreva uma cidade válida'})

        for key, value in data['main'].items():
            if key == 'temp':
                aux = value - 273.15
                data['main'][key] = round(aux,0)

        data['main']['description'] = data['weather'][0]['description']
        data['main']['name'] = city

        return render(request, 'weather.html', {'data':data['main']})

    return render(request, "weather.html")


 