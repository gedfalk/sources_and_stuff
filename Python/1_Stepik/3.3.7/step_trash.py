# Обзорно об интернете...
'''
Из данного на вход html-файла выцепить все сайты

'''

import re
import requests


pattern = r'href=[\"\'](.+?)/*[\"\'].*?>'


url = 'http://pastebin.com/raw/7543p0ns'
res = requests.get(url)
source = res.text


#with open('input.txt', 'r') as inp:
#    source = inp.read()

# Обрабатываем исключение "относительных ссылок href="../""
source = re.sub(r'<a .+\.\./.+?>', '', source)

#print(source)

# Вычищаем из url "приставку" в лице протокола обмена и www
source = re.sub(r'https*://|ftp://', '', source)

    #print(source)

# Вычищаем из url "суффикс", или то, что следует после домена 
source = re.sub(r'(/|:).+?([\"\'])', r'\2', source)

print(source)

urls = re.findall(pattern, source)

print(*urls, sep='\n')

urls_final = []

for u in sorted(urls):
    if u not in urls_final:
        urls_final.append(u)

print()
print(*urls_final, sep='\n')