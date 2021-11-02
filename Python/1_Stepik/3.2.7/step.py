# Регулярные выражения в Python

'''
Все упражнения от 3.2.7 до 3.2.15

'''


import sys
import re


'''
pattern = 'cat'

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 1:
        print(line)
'''


'''
pattern = r'\bcat\b'
pattern = r'z...z'
pattern = r'\\'
pattern = r'\b(\w+)\1\b'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)

'''


'''
pattern = 'human'
replace = 'computer'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, replace, line))
'''


'''
pattern = r'\ba+\b'
replace = 'argh'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, replace, line, count=1, flags=re.IGNORECASE))
'''


#pattern = r'\b(\w)(\w)'
#replace = r'\2\1'

pattern = r'(\w)\1+'
replace = r'\1'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, replace, line))

