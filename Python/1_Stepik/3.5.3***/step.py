# API
'''
Восользоваться API сайта numbersapi.com и выяснить, интересно ли заданное число

'''

import requests
import re

url_api = 'http://numbersapi.com/'
type_u = 'math'
#type_u = 'trivia'

with open('dataset_24476_3.txt', 'r') as inp:
    numbers = inp.read().split()
    numbers = [int(numbers[i]) for i in range(len(numbers))]

    for number in numbers:

        params = {
            'number' : number,
            'type' : type_u,
            'json' : 'json'
        }

        res = requests.get(url_api + str(params['number']) + '/' + params['type'], params=params['json'])
        data = res.json()

        #print('Interesting' if data['found'] else 'Boring')
        print(re.sub(r'^(\d+)', r'_\1_', data['text']) if data['found'] else '\t' + str(number) + ' is Boooooriiing')
