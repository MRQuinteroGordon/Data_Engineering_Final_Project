import requests
import json
# import math
import datetime
import time
from dotenv import load_dotenv
import os
# import pandas as pd


load_dotenv()
api_key = os.getenv("WEATHER_KEY")
zipcode = 84123
country = "US"
lat = 0
lon = 0
start_date = "03/18/23"
end_date = "03/18/24"

def get_latlons(zipcode, country, key):
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{country}&appid={key}"
    response = requests.get(url).json()
    latlon = [response['lat'], response['lon']]
    print(response)
    return latlon

def get_weather(lat, lon, date, key):
    units = "imperial"
    url = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date}&appid={key}&units={units}"
    response = requests.get(url).json()
    return response

def create_date_list(start, end):
    start_date = datetime.datetime.strptime(start, "%m/%d/%y")
    end_date = datetime.datetime.strptime(end, "%m/%d/%y")

    date_list = [(d.strftime("%Y-%m-%d")) for d in
             (start_date + datetime.timedelta(days=i) for i in range((end_date - start_date).days + 1))]

    return date_list

def append_to_json(new_data, filename='data.json'):
    try:
        # Read existing data from the file
        with open(filename, 'r') as file:
            file_data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, create an empty list
        file_data = []

    # Append new_data to the existing data
    file_data.append(new_data)

    # Write the updated data back to the file
    with open(filename, 'w') as file:
        json.dump(file_data, file, indent=4)

def weather_history(zipcode, country, key, start, end):
    coords = get_latlons(zipcode, country, api_key)
    dates = create_date_list(start, end)
    for date in dates:
        weather = get_weather(coords[0], coords[1], date, key)
        append_to_json(weather)
    print("Process successfully finished... I think.")

weather_history(zipcode, country, api_key, start_date, end_date)

# hist_weather = get_weather(coords[0], coords[1], unix_start, unix_end, api_key)
# with open('historicalweather.json', 'w') as f:
#     json.dump(hist_weather, f)

# dates = create_date_list()
# print(len(dates))

# weather = get_weather(coords[0], coords[1], dates[0], api_key)
# print(weather)

# coords = get_latlons(zipcode, country, api_key)
# print(f"84123 coordinates: latitude {coords[0]} longitude: {coords[1]}")








#example geocoding api call:
# "http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={API key}"

# "https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&cnt={cnt}&appid={API key}"

# "https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={API key}"