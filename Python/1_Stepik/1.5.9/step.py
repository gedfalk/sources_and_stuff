class Buffer:
	def __init__(self):
		self.b = []

	def add(self, *a):
		self.b.extend(a)
		while len(self.b) >= 5:
			print(sum(self.b[0:5]))
			del self.b[0:5]

	def get_current_part(self):
		return self.b




