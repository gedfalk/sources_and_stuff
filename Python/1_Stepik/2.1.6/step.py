def divide(x, y):
	try:
		print(x / y)
	except ZeroDivisionError as e:
		print(type(e).__name__)

divide(10, 0)