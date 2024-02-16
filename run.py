from app import WeatherApp
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
weather_app = WeatherApp(api_key)
weather_app.run()
