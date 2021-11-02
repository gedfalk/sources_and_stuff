tree = {}
TREE = []

def define(F, ch):
	if F in tree[ch]:
		return 'Yes'
	else:
		for i in tree[ch]:
			if define(F, i) == 'Yes':
				return define(F, i)

	return 'No'


n = int(input())

for i in range(n):
	string = input().split(' :')
	if len(string) == 1:
		tree[string[0]] = []
	else:
		tree[string[0]] = string[1].split()

n = int(input())
for i in range(n):
	ch = input()
	TREE.append(ch)
	check = False
	for j in TREE:
		if define(j, ch) == 'Yes':
			check = True

	if check == True:
		print(ch)


#print(tree)