import json
import requests

def get_weather(location):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    temperature = data['main']['temp']
    weather = data['weather'][0]['main']
    return f"The temperature in {location} is {temperature}°C and the weather is {weather}"

location = input("Enter a location: ")
weather = get_weather(location)
print(weather)
