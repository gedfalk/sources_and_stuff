import simplecrypt

with open('encrypted.bin', 'rb') as inp:
	encrypted = inp.read()

with open('passwords.txt', 'rb') as pas:
	for string in pas:
		s = string.split()[0]
		print(s)
		try:
			print(simplecrypt.decrypt(s, encrypted).decode('utf8'))
		except:
			print('Failed')
		
