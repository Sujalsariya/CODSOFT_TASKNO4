import requests
import os
from datetime import datetime

user_api = os.environ['current_weather_data']
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
# print (complete_api_link)
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid city: {}, Please check your city name".format(location))
    
else:
    #create some inconstant value to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather States for - {}.format(location.upper(),date_time)")
print("-------------------------------------------------------------")

print("Current temperature is :{:.2f} deg C".format(temp_city))
print("Current weather desc:", weather_desc)
print("Current Hunidity:",hmdt, '%')
print("Current wind speed:", wind_spd, 'kmph')






































#city = input('input the city name')
#print (city)

#print('Displaying weather report for: ' + city)

#url = 'https://wttr.in/{}'.format(city)

