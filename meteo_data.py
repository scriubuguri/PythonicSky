#!/usr/bin/env python
#Weather data and forecast for your city
#Author: scriubuguri

import json
import requests


#function to get weather data
def get_weather(city, units, param):
    API_KEY = "your_api_key":
    FULL_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}".format(
        city=city,
        api_key=API_KEY,
        units=units
    )

    response = requests.get(FULL_URL)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Error encountered when calling the weather API")


#functions to print weather's parameters
def temp_funct(city, units, param):
    final_data = get_weather(city, units, param)
    if final_data:
        current_temp = int(final_data['main']['temp'])
        print("-Current temperature: {temp} C".format(temp=current_temp))
    else:
        print("Error fetching data")

def wind_funct(city, units, param):
    final_data = get_weather(city, units, param)
    if final_data:
        wind_speed = int(final_data['wind']['speed'])
        print("-Wind speed: {speed} m/s".format(speed=wind_speed))
    else:
        print("Error fetching data")

def humidity_funct(city, units, param):
    final_data = get_weather(city, units, param)
    if final_data:
        humidity = int(final_data['main']['humidity'])
        print("-Humidity: {humidity} %".format(humidity=humidity))
    else:
        print("Error fetching data")

def clouds_funct(city, units, param):
    final_data = get_weather(city, units, param)
    if final_data:
        clouds = int(final_data['clouds']['all'])
        print("-Cloudiness: {clouds} %".format(clouds=clouds))
    else:
        print("Error fetching data")

#main function to call all the functions above  
def main():
    parser = argparse.ArgumentParser(description="Get weather information for a city.")
    parser.add_argument("-c", default="Bucharest", help="City name")
    parser.add_argument("-u", choices=["metric", "imperial", "standard"], default="metric", help="Temperature units (default: metric)")
    parser.add_argument("-p", choices=["t", "w", "h", "c"], default="t", help="Weather parameter (default: t)")

    args = parser.parse_args()

    if args.p == "t":
        temp_funct(args.c, args.u, args.p)
    elif args.p == "w":
        wind_funct(args.c, args.u, args.p)
    elif args.p == "h":
        humidity_funct(args.c, args.u, args.p)
    elif args.p == "c":
        clouds_funct(args.c, args.u, args.p)

if __name__ == "__main__":
    main()


