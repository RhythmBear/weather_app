import requests
import os


class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',  
        }

        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                return data
            else:
                print(f"Error: {data['message']}")
                return None

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def display_weather(self, weather_data):
        if weather_data:
            print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Description: {weather_data['weather'][0]['description']}")
            print(f"Humidity: {weather_data['main']['humidity']}%")
            print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            print("Unable to fetch weather information.")

    def run(self):
        city = input("Enter the city name: ")
        weather_data = self.get_weather(city)
        self.display_weather(weather_data)
