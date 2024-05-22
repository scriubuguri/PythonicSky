#!/usr/bin/env python
# Weather data and forecast for your city
# Author: scriubuguri

import requests
import argparse
import os


class Weather:
    def __init__(self, city, system="metric", verbose=False):
        self.city = city
        self.system = system
        self.verbose = verbose
        self.api_key = os.environ.get('weather_data_key', 'your_api_key')
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.system_options = {"metric": "C", "imperial": "F", "standard": "K"}
        self.weather_data = self.get_weather()

    def get_weather(self):
        params = {
            'q': self.city,
            'appid': self.api_key,
            'units': self.system
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error encountered when calling the weather API")
            return None

    def display_data(self, data_key, data_label, unit=""):
        if self.weather_data:
            data_value = self.weather_data['main'].get(data_key) if data_key in self.weather_data['main'] else self.weather_data['wind'].get(data_key) if data_key == 'speed' else self.weather_data['clouds'].get('all')
            if data_value is not None:
                ante = ""
                if self.verbose:
                    ante = f"{data_label} in {self.city} is: "
                print(f"{ante}{data_value} {unit}")
            else:
                print(f"Error fetching {data_label.lower()} data")
        else:
            print("Error fetching data")

    def display_temperature(self):
        units = self.system_options.get(self.system, "")
        self.display_data('temp', "Current temperature", units)

    def display_wind(self):
        self.display_data('speed', "Wind speed", "m/s")

    def display_humidity(self):
        self.display_data('humidity', "Humidity", "%")

    def display_cloudiness(self):
        self.display_data('all', "Cloudiness", "%")


def main():
    parser = argparse.ArgumentParser(description="Get weather information for a city.")
    parser.add_argument("-c", default="Bucharest", help="City name")
    parser.add_argument("-u", choices=["metric", "imperial", "standard"], default="metric", help="Temperature system (default: metric)")
    parser.add_argument("-p", choices=["t", "w", "h", "c"], default="t", help="Weather parameter (default: t)")
    parser.add_argument("-v", action="store_true", help="Verbose mode")

    args = parser.parse_args()

    weather = Weather(city=args.c, system=args.u, verbose=args.v)

    if args.p == "t":
        weather.display_temperature()
    elif args.p == "w":
        weather.display_wind()
    elif args.p == "h":
        weather.display_humidity()
    elif args.p == "c":
        weather.display_cloudiness()


if __name__ == "__main__":
    main()
