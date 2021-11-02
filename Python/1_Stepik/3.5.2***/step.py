#!/usr/bin/python3

import requests

api_url = 'http://api.openweathermap.org/data/2.5/weather'

city = input('City?\n')

params = {
    'q': city,
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': 'metric'
}

res = requests.get(api_url, params=params)

data = res.json()
template = 'Current temperature in {} is {}'
print(template.format(city, data['main']['temp']))