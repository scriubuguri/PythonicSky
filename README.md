#meteo_data.py

A quick and simple CLI tool that gets weather data from an API.
This program allows you to retrieve weather details and forecasts for a specific city using the OpenWeatherMap API. It provides information such as current temperature, wind speed, humidity, and cloudiness.

## Features

- Retrieve weather data for a city using the OpenWeatherMap API.
- Specify the temperature units (metric, imperial, or standard).
- Choose the weather parameter to display (temperature, wind speed, humidity, or cloudiness).

## Requirements

- Python 3.x
- `requests` module
- `json` module
- `argparse` module

## Installation


1. Clone this repository

Open a terminal and change the current directory to the location where you want to clone the repository.
Type the following command and press enter:

```bash
git clone https://github.com/scriubuguri/meteodata.git
```

2. Sign up to OpenWeather [here](https://home.openweathermap.org/users/sign_up) and get your API key.

3. Open the `meteodata.py` file and add your API key on the *API_KEY* variable.


## Usage

Run the program using the following command:

```bash
python meteo_data.py [-c <city>] [-u <units>] [-p <parameter>]
```

or  

```bash
chmod +x meteo_data.py
./meteo_data.py [-c <city>] [-u <units>] [-p <parameter>]
```

The available options are:

- `-c <city>`: Specify the name of the city for which you want to retrieve weather information. If not provided, the default city is "Bucharest".
- `-u <units>`: Specify the temperature units to display. Available options are "metric" (Celsius), "imperial" (Fahrenheit), and "standard" (Kelvin). The default unit is "metric".
- `-p <parameter>`: Specify the weather parameter to display. Available options are "t" (temperature), "w" (wind speed), "h" (humidity), and "c" (cloudiness). The default parameter is "t".

## Example

- Retrieve the current temperature for Pitesti in Celsius:
```bash
python meteo_data.py -c Pitesti -u metric -p t
```

- Retrieve the wind speed for Timisoara in miles per hour:
```bash
python meteo_data.py -c "Timisoara" -u imperial -p w
```

- Retrieve the humidity for Iasi:
```bash
python meteo_data.py -c Iasi -p h
```

- Retrieve the cloudiness for Ploiesti:
```bash
python meteo_data.py -c Ploiesti -p c
```

## Author

- **scriubuguri**

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
