import requests
import json

city= input("Enter the name of the city you want to check weather:\n")
url=f"https://api.weatherapi.com/v1/current.json?key=cd65c9b756e3402096e95035242701&q={city}"
h=requests.get(url)
#print(h.text)

weatherDictionary=json.loads(h.text)
print("Country:",weatherDictionary ["location"]["country"],"\n","Region:",weatherDictionary ["location"]["region"],"\n","Temp In °C:", weatherDictionary["current"]["temp_c"],"°C\n","Temp In °F:", weatherDictionary["current"]["temp_f"],"°F\n","Cloud:",weatherDictionary["current"]["cloud"],"\n","Humidity:",weatherDictionary["current"]["humidity"],"\n","Wind Direction:",weatherDictionary["current"]["wind_dir"],"\n")

