import time

class Loggable:
	def log(self, msg):
		print(str(time.ctime()) + ': ' + str(msg))

class LoggableList(Loggable, list):
	def append(self, x):
		super(LoggableList, self).append(x)
		super(LoggableList, self).log(self[-1])

l = Loggable()
l.log('Пипец какой-то!!')

ls = LoggableList()
ls.extend([1, 2, 3, 4])
ls.append(5)