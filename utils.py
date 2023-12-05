#!/usr/bin/env python

import datetime

# request parameters
MAIN_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "your_api_key"
CITY = "Bucharest"
UNITS = "metric"

FULL_URL = "{main_url}q={city}&appid={api_key}&units={units}".format(
    main_url=MAIN_URL,
    city=CITY,
    api_key=API_KEY,
    units=UNITS,
)

def get_date_and_time(timestamp):
    dt = datetime.datetime.utcfromtimestamp(timestamp).strftime('%d %b %Y %H:%M:%S')
    return dt
