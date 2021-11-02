rel = dict()

def define(F, ch):
	if F in rel[ch] or F == ch:
		return 'Yes'
	else:
		for i in rel[ch]:
			if define(F, i) == 'Yes':
				return define(F, i)

	return 'No'



n = int(input())
for i in range(n):
	s = input().split(' :')
	if len(s) == 1:
		rel[s[0]] = []
	else:
		rel[s[0]] = s[1].split()


print(rel)

n = int(input())
for i in range(n):
	F, ch = input().split()
	print(define(F, ch))