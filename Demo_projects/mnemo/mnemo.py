# на вход подаётся словарь русского языка
# на выход отдется число согласно буквенно-цифровому коду


_VOWELS = 'аяоёэеыиую'
_CONS_DIG = {'г': 1, 'ж': 1,
			 'д': 2, 'т': 2,
			 'к': 3, 'х': 3,
		 	 'ч': 4, 'щ': 4,
			 'п': 5, 'б': 5,
			 'ш': 6, 'л': 6,
			 'с': 7, 'з': 7,
			 'в': 8, 'ф': 8,
			 'р': 9, 'ц': 9,
			 'м': 0, 'н': 0,
			 'ь': '', 'ъ': '', 'й': ''}
_NUMBERS = {}		


# шифрует слово в буквенно-цифровой код (БЦК)
def _cipher(word: str) -> str:
	res = ''
	for ch in word.lower():
		if ch in _CONS_DIG:
			res += str(_CONS_DIG[ch])
	return res

# принимает на вход файл со словами, создаёт на его основе словарь
def _create_dict(file: str) -> dict:
	_Dict = dict()
	with open(file, 'r')  as _input_file:
		for line in _input_file:
			_xyz = _cipher(line)
			if _xyz not in _Dict:
				_Dict[_xyz] = [line.rstrip()]
			else:
				_Dict[_xyz].append(line.rstrip())
	return _Dict	


def main() -> None:
	_input_file = 'source/test_russian.txt'
	_output_file = 'source/test_rus_dict.txt'
	'''
	_D = _create_dict('source/russian.txt')
	with open('source/rus_dict.txt', 'w') as _output_file:
		#_L = sorted(_D, key=lambda x: len(x))
		_L = sorted(_D)
		for key in _L:
			value = _D[key]
			line = f'{key}: {value}\n'
			#_output_file.write(line)
	'''	
	print(_cipher('бытие'), _cipher('определяет'), _cipher('сознание'))


if __name__ == "__main__":
	main()

