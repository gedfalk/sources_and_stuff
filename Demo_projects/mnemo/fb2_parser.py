# считывает книгу в формате FB2


import xml.etree.ElementTree as ET


def main() -> None:
	with open('source/books/war_and_peace.fb2', 'br') as _file:
		for i in range(100):
	#		print(_file.readline())
			pass

	with open('source/books/war_and_peace_output.txt', 'w') as _output:
		_fb2 = ET.parse('source/books/war_and_peace.fb2')
		_root = _fb2.getroot()
		for node in _root.iter():
			try:
				_output.write(node.text)
			except:
				print(node.text)
				_output.write('_____Unable to read_____')
				pass
		print("hell")



if __name__ == "__main__":
	main()