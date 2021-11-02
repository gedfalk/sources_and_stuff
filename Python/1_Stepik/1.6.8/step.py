class ES(list):
	def sum(self):
		self.append(self.pop(-1) + self.pop(-1))

###

stack = ES()
stack.extend([1, 2, 3, 4, 5])
stack.sum()
print(stack)