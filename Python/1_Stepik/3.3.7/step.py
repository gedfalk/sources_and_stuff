# Та же задача, что и step_trash.py, начатая с нуля

import re
import requests


url = 'http://pastebin.com/raw/7543p0ns'

#with open('input.txt', 'r') as inp:
#    text = inp.read()


pattern = r'<a.+?href=[\'\"](.+?)[\'\"].*?>'

# Запрашиваем страницу и выцепляем все ссылки в список urls
res = requests.get(url)
urls = re.findall(pattern, res.text)

#urls = re.findall(pattern, text)

final_list = []

#print(res.text, '\n')


# Проходимся по списку адресов и "вычищаем" до блеска
for u in urls:
    if '../' in u:
        continue

    # Удаляем "приставку" в виде протокола
    s = re.sub(r'https*://|ftp://', r'', u)

    # Удаляем "суффикс"
    s = re.sub(r'(/|:).*', r'', s)
    
    if s not in final_list:
        final_list.append(s)


print(*sorted(final_list), sep='\n')


'''
А это "Пример правильного решения" от создателей курса.
Обёрта красивая, но Кааааак читать такое регулярное выражение человеку со
стороны - мой мозг отказывается понимать:

r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)
------------------------------------------------


import re
import requests

resp = requests.get(input()).text
sites = set()
for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
    sites.add(site)

for site in sorted(sites):
    print(site)

'''