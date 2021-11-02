# API
'''
Делаем запрос к artsy.net через API, получая информацию о художниках

'''


import requests
import json

# Идентификационный номер и "пароль", полученные из artsyAPI
client_id = 'c05475dc1bad285eadc5'
client_secret = 'a82581ea8d37bdaabe1d79c8c18e7998'

# Формируем запрос из этой информации
data = {
    'client_id': client_id,
    'client_secret': client_secret  
}

# Получаем токен с сайта
res = requests.post('https://api.artsy.net/api/tokens/xapp_token', data)
j = json.loads(res.text)
token = j['token']






# ДАЛЕЕ
# Имея на руках _токен_ формируем запрос по художникам, прибавляя к запросу _токен_
headers = {
    'X-Xapp-Token': token
}

artists = {}
years = []
with open('dataset_24476_4.txt', 'r') as inp:
    for artist_id in inp:
        res = requests.get('https://api.artsy.net/api/artists/' + artist_id.strip(), headers=headers)
        j = json.loads(res.text)

        birthday = j['birthday']
        name = j['sortable_name']

        if birthday not in years:
            years.append(birthday)

        if birthday not in artists:
            artists[birthday] = [name]
        else:
            artists[birthday].append(name)
            artists[birthday] = sorted(artists[birthday])

        #print(name, birthday)

for y in sorted(years):
    for a in artists[y]:
        print(a)
        