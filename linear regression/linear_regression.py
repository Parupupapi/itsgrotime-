# linear_regression_model.py

from sklearn.linear_model import LinearRegression
import joblib
import pandas
import numpy as np
import requests
import json

def fetch_forecast_data(api_key, lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly&units=imperial&appid={api_key}'
    response = requests.get(url)
    return response.json()

api_key = 'e4d474a322c0877f50ad1ce9bfa13d83'
latitude = 37.7749  # Replace with your actual latitude
longitude = -122.4194  # Replace with your actual longitude

forecast_data = fetch_forecast_data(api_key, latitude, longitude)
print(json.dumps(forecast_data, indent=2))

print("Keys in forecast_data:", forecast_data.keys())

# def process_forecast_data(forecast_data):
#     # Implement your processing logic here
#     # Example: Assigning a success score of 0.8 if temperature is above 70 and humidity is below 60
#     processed_data = [
#         {
#             'date': day['dt'],
#             'temperature': day['temp']['max'],
#             'humidity': day['humidity'],
#             'sunlight': day['sunrise'],  # Replace with actual sunlight data
#             'success_score': 0.8 if day['temp']['max'] > 70 and day['humidity'] < 60 else 0.5
#         }
#         for day in forecast_data['daily']
#     ]

#     return processed_data

# # Example Usage
# processed_forecast = process_forecast_data(forecast_data)
# print(json.dumps(forecast_data, indent=2))
