def get(namespace, arg):
	if arg in varrr[namespace] or namespace == 'None':
		return namespace
	for key,value in child.items():
		if namespace in value:
			return(get(key, arg)) 
	#return 0

child = {}
varrr = {}

child['None'] = ['global']
child['global'] = []

varrr['global'] = []
varrr['None'] = []

n = int(input())

for i in range(n):
	op, namespace, arg = input().split()
	if op == 'create':
		child[arg].append(namespace)
		child[namespace] = []
		varrr[namespace] = []
	if op == 'add':
		varrr[namespace].append(arg)
	if op == 'get':
		print(get(namespace, arg))


#print(child)
#print(varrr)