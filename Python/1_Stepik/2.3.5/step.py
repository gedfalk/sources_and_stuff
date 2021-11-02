# Итераторы и генераторы
# Генерация простых чисел через itertools

import itertools

def primes():
	yield 2
	n = 3
	while True:
		i = 2
		while i < n:
			if n % i != 0:
				i += 1
			else:
				break

		if i == n:
			yield n
		n += 1	


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
