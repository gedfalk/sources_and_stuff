# Обзорно об интернете: http-запросы, html-страницы и requests
'''
Можно ли перейти со страницы А на страницу В за два перехода

'''


# Поиск всех url-адресов в тексте и возвращение списка
def find_url(text):
    lst = re.findall(pattern, text)
    #print('в данном text ', text, '\nсписок адресов выглядит так ', lst)
    return lst

# Получить исходный код страницы по url в виде текста
def get_text(url):
    res = requests.get(url)
    #print('по адресу ', url, '\n text = ', res.text)
    return res.text


import requests
import re

#url_A = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
#url_B = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'



pattern = '.+href="(.+?)">.+'
res = 'No'

url_A = input()
url_B = input()

text1 = get_text(url_A)
lst1 = find_url(text1)
for u in lst1:
    text2 = get_text(u)
    lst2 = find_url(text2)

    if url_B in lst2:
        res = 'Yes'

print(res)