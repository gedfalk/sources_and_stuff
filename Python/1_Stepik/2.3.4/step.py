# Итераторы и генераторы
# Реализовать функцию multifilter

class multifilter:
	def judge_half(pos, neg):
		if pos >= neg:
			return True
		else:
			return False

	def judge_any(pos, neg):
		if pos >= 1:
			return True
		else:
			return False

	def judge_all(pos, neg):
		if neg == 0:
			return True
		else:
			return False

	def __init__(self, iterable, *funcs, judge=judge_any):
		self.table = [[0, 0] for i in iterable]
		self.lst = []
		for f in funcs:
			for i in range(len(iterable)):
				if f(iterable[i]) == True:
					self.table[i][0] += 1
				else:
					self.table[i][1] += 1
		
		for i in range(len(iterable)):
			if judge(self.table[i][0], self.table[i][1]) == True:
				self.lst.append(iterable[i])

	def __iter__(self):
		return iter(self.lst)
			
		

def mul2(x):
	return x % 2 == 0

def mul3(x):
	return x % 3 == 0

def mul5(x):
	return x % 5 == 0


a = [i for i in range(31)]

'''
a = multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)
print(type(a))
'''

print(list(multifilter(a, mul2, mul3, mul5))) 

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# [0, 30]