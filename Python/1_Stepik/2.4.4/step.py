# Работа с файловой системой и файлами
# "Перевернуть" входной файл

with open('dataset_24465_4.txt', 'r') as inp:
	Data = inp.read().splitlines()

with open('output.txt', 'w') as out:
	text = '\n'.join(Data[::-1])
	out.write(text)

