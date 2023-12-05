#!/usr/bin/env python
#Weather data and forecast for your city
#Author: scriubuguri

import json
import requests

from utils import FULL_URL, get_date_and_time


# interogate the API
response = requests.get(FULL_URL)

if response.status_code == 200:
    weather_data = response.json()

    menu_structure = [
        "--- Bucharest weather data --- ",
        "Date: {date_and_time}".format(date_and_time=get_date_and_time(weather_data['dt'])),
        "a) Temperature",
        "b) Cloudiness and visibility",
        "c) Humidity and pressure",
        "d) Wind",
        "q) Quit"
    ]
    print("\n".join(menu_structure))

    while True:
        selected_option = input("Please select an option from a to d:")
        if selected_option == "a":
            rasp_a = [
                "-Current temperature: {current_temp} C".format(current_temp=weather_data['main']['temp']),
                "-Real feel: {real_feel} C".format(real_feel=weather_data['main']['feels_like']),
                "-Max temperature: {max_temp} C".format(max_temp=weather_data['main']['temp_max']),
                "-Min temperature: {min_temp} C".format(min_temp=weather_data['main']['temp_min'])
            ]
            print("\n"+"The required information are: "+"\n"+"\t"+rasp_a[0]+"\n"+"\t"+rasp_a[1]+"\n"+"\t"
                  +rasp_a[2]+"\n"+"\t"+rasp_a[3]+"\n")
            print("\n".join(menu_structure))

        elif selected_option == "b":
            rasp_b = ["-Cloudiness: {clouds} %".format(clouds=weather_data['clouds']['all']),
                      "-Visibility: {visibility} m".format(visibility=weather_data['visibility'])]
            print("\n"+"The required information are: " +"\n"+"\t"+rasp_b[0]+"\n"+"\t"+rasp_b[1]+"\n")
            print("\n".join(menu_structure))

        elif selected_option == "c":
            rasp_c = ["-Humidity: {humidity} %".format(humidity=weather_data['main']['humidity']),
                      "-Pressure: {pressure} mmHg".format(pressure=weather_data['main']['pressure'])]
            print("\n"+"The required information are: " +"\n"+"\t"+rasp_c[0]+"\n"+"\t"+rasp_c[1]+"\n")
            print("\n".join(menu_structure))

        elif selected_option == "d":
            rasp_d = ["-Wind speed: {speed} m/s".format(speed=weather_data['wind']['speed']),
                      "-Wind direction: {deg} degrees".format(deg=weather_data['wind']['deg'])]
            print("\n"+"The required information are: " +"\n"+"\t"+rasp_d[0]+"\n"+"\t"+rasp_d[1]+"\n")
            print("\n".join(menu_structure))
        elif selected_option == "q":
            break
        else:
            print("\n"+"Your selected option is not valid. \tPlease select a letter from a to d."+"\n")
            print("\n".join(menu_structure))
            selected_option = input("Please select an option from a to d:")

else:
    weather_data = None
    print("Error encountered when calling the weather API: {err}".format(err=response.text))
