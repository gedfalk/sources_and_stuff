# Стандартные методы и функции для строк
"""
Меняем в изначальное строке _s_ вхождения a на b, пока это возможно

"""

s = input()
a = input()
b = input()


i = 0
while a in s:
    s = s.replace(a, b)
    i += 1
    if i > 1000:
        break

if i > 1000:
    print('Impossible')
else:
    print(i)





