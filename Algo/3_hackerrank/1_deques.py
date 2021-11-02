# deque

from collections import deque

test = ['append 1',
        'append 2',
        'append 3',
        'appendleft 4',
        'pop',
        'popleft']

n = len(test)
d = deque()

for line in test:
    if ' ' in line:
        com, num = line.split()
        eval('d.'+com+'('+num+')')
        print(d)
    else:
        com = line
        eval('d.'+com+'()')
        print(d)

print(*d, sep=' ')

