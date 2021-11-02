# XML, библиотека ElementTree, библиотека lxml
'''
Принять на вход xml-файл "пирамиды из кубиков" в формате строки и реурсивно 
оббежать её

'''


import xml.etree.ElementTree as et


def runner(root, value):
    root.set('value', value)
    # Узнаём цвет кубика
    color = root.get('color')
    # Заносим в словарь цветов кубиков
    if color not in cube_value:
        cube_value[color] = value
    else:
        cube_value[color] += value

    # Собственно запускаем рекурсию
    for child in root:
        runner(child, value+1)


xml_string = '<cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue"></cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red"><cube color="blue"></cube></cube></cube>'
cube_value = {}
root = et.fromstring(xml_string)


runner(root, 1)

for el in root.iter():
    print(el.tag, el.attrib)

print(cube_value['red'], cube_value['green'], cube_value['blue'])

