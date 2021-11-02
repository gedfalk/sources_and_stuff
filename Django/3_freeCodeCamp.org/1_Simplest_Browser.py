import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = 'data.pr4e.org'
mysocket.connect((url, 80))
cmd = ('GET http://' + url + '/page1.htm HTTP/1.0\r\n\r\n').encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:                
        break
    print(data.decode(), end='')

mysocket.close()


'''

Импортируем библиотеку

Открываем свой сокет
Соединяемся с сервером
Отправляем запрос GET

Получаем ответ и выводим

Закрываем сокет

'''