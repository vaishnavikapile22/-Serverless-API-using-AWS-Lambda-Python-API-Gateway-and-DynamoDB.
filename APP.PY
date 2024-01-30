import requests
import os
from datetime import datetime

# Weather API
weather_api_key = os.environ['api']
location = input("Enter city for weather: ")
weather_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={weather_api_key}"


# Fetching Weather Data
weather_response = requests.get(weather_api_link)
weather_data = weather_response.json()

news_api_key = os.environ['NEWS_API_KEY']
location = input("Enter the cityfor newscl: ")
news_api_link = f"https://newsapi.org/v2/everything?q={location}&apiKey={news_api_key}"


# Fetching News Data
news_response = requests.get(news_api_link)
news_data = news_response.json()

# Extracting Weather Data
temp_city = ((weather_data['main']['temp']) - 273.15)
weather_desc = weather_data['weather'][0]['description']
hmdt = weather_data['main']['humidity']
wind_spd = weather_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# Display Weather Information
print ("-------------------------------------------------------------")
print (f"Weather Stats for - {location.upper()}  || {date_time}")
print ("-------------------------------------------------------------")
print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :", weather_desc)
print ("Current Humidity      :", hmdt, '%')
print ("Current wind speed    :", wind_spd ,'kmph')

# Display News Information
print ("-------------------------------------------------------------")
print (f"News for - {location.upper()}")
print ("-------------------------------------------------------------")
for article in news_data['articles']:
    print(article['title'])
