# Распространённые форматы текстовых файлов: CSV, JSON
'''
Сделать выборку по преступлениям из Огромного датасета

'''

import csv


data = {}
with open('Crimes.csv') as inp:
    reader = csv.reader(inp)
    for line in reader:
        date = line[2]
        # Конструкция вытаскивает из даты '20/03/2002 09:00:27' год 2002
        year = date.split()[0].split('/')[-1]
        crime = line[5]

        if crime not in data:
            data[crime] = 0
        else:
            data[crime] += 1

max_value = 0
max_crime = ''
for key, value in data.items():
    if value >= max_value:
        max_value = value
        max_crime = key

print(max_crime, max_value)