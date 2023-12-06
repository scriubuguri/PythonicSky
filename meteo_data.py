#!/usr/bin/env python
#Weather data and forecast for your city
#Author: scriubuguri

import json
import requests
import argparse
import os


#function to get weather data
def get_weather(param):
    if 'weather_data_key' in os.environ:
        API_KEY = os.environ['weather_data_key']
    else:
        API_KEY = "your_api_key"

    FULL_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={system}".format(
        city=param['city'],
        api_key=API_KEY,
        system=param['system']
    )

    response = requests.get(FULL_URL)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Error encountered when calling the weather API")


#functions to print weather's parameters
def temp_funct(param):
    final_data = get_weather(param)
    if final_data:
        current_temp = int(final_data['main']['temp'])
        if param['system'] == "metric":
            units = "C"
        elif param['system'] == "imperial":
            units = "F"
        elif param['system'] == "standard":
            units = "K"
        if param['verbose'] == True:
            ante = "Current temperature in {city} is: ".format(city=param['city']) 
        elif param['verbose'] == False:
            ante = ""

        print("{ante}{temp} {units}".format(ante=ante, temp=current_temp, units=units))
    else:
        print("Error fetching data")

def wind_funct(param):
    final_data = get_weather(param)
    if final_data:
        wind_speed = int(final_data['wind']['speed'])
        if param['verbose'] == True:
            ante = "Wind speed in {city} is: ".format(city=param['city'])
        elif param['verbose'] == False:
            ante = ""
        print("{ante}{speed} m/s".format(ante=ante, speed=wind_speed))
    else:
        print("Error fetching data")

def humidity_funct(param):
    final_data = get_weather(param)
    if final_data:
        humidity = int(final_data['main']['humidity'])
        if param['verbose'] == True:
            ante = "Humidity in {city} is: ".format(city=param['city'])
        elif param['verbose'] == False:
            ante = ""
        print("{ante}{humidity} %".format(ante=ante,humidity=humidity))
    else:
        print("Error fetching data")

def clouds_funct(param):
    final_data = get_weather(param)
    if final_data:
        clouds = int(final_data['clouds']['all'])
        if param['verbose'] == True: 
            ante = "Cloudiness in {city} is: ".format(city=param['city'])
        elif param['verbose'] == False:
            ante = ""
        print("{ante}{clouds} %".format(ante=ante, clouds=clouds))
    else:
        print("Error fetching data")

#main function to call all the functions above  
def main():
    parser = argparse.ArgumentParser(description="Get weather information for a city.")
    parser.add_argument("-c", default="Bucharest", help="City name")
    parser.add_argument("-u", choices=["metric", "imperial", "standard"], default="metric", help="Temperature system (default: metric)")
    parser.add_argument("-p", choices=["t", "w", "h", "c"], default="t", help="Weather parameter (default: t)")
    parser.add_argument("-v", action="store_true", help="Verbose mode")

    args = parser.parse_args()
    #make a dictionary with the parameters so that we can send only one object to functions:
    param = {
        'city': args.c,
        'system': args.u,
        'param': args.p,                    
        'verbose': args.v
    }


    if args.p == "t":
        temp_funct(param)
    elif args.p == "w":
        wind_funct(param)
    elif args.p == "h":
        humidity_funct(param)
    elif args.p == "c":
        clouds_funct(param)

if __name__ == "__main__":
    main()


