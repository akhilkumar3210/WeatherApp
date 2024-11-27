from django.shortcuts import render
import requests
import math,datetime
# Create your views here.
def index(req):
    cityname='kochi'
    
    if req.method=='POST':
        cityname=req.POST['city']
        api_key='360e4bc3865e745ec844bd7ec054ca11'
        url=f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'
        weather=requests.get(url)
        weather_data=weather.json()
        
        try:
            data={
                'city':cityname,
                'description':weather_data['weather'][0]['description'],
            }
        except:
            cityname='kochi'
        
        
    api_key='360e4bc3865e745ec844bd7ec054ca11'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'
    weather=requests.get(url)
    weather_data=weather.json()
    dataobj= datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
    dataobj1= datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
    data={
        'city':cityname,
        'description':weather_data['weather'][0]['description'],
        'temp':math.floor(weather_data['main']['temp']-273.15),
        'feels_like':math.floor(weather_data['main']['feels_like']-273.15),
        'temp_min':math.floor(weather_data['main']['temp_min']-273.15),
        'temp_max':math.floor(weather_data['main']['temp_max']-273.15),
        'pressure':weather_data['main']['pressure'],
        'humidity':weather_data['main']['humidity'],
        'sunrise':dataobj.strftime('%H:%M:%S'),
        'sunset':dataobj1.strftime('%H:%M:%S'),
        
    
    }
    return render(req,'index.html',{'data':data})
        
    