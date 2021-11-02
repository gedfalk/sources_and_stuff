# Распространённые форматы текстовых файлов: CSV, JSON
'''
Опять Е###ИЕ наследования классов!!!
По-моему это просто издевательство

'''

import json

# Импортированная функция из степа 1.6... на определение "родительства" 
def define(F, ch):
    if F in tree[ch] or F == ch:
        return 'Yes'
    else:
        for i in tree[ch]:
            if define(F, i) == 'Yes':
                return define(F, i)

    return 'No'


#example = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
#example = '[{"name": "A", "parents": ["B", "C", "D"]},{"name": "E", "parents": ["F", "G"]},{"name": "I", "parents": ["E", "F", "Y", "D", "G"]},{"name": "B", "parents": ["I", "Y", "D", "G"]},{"name": "F", "parents": ["D", "Z"]},{"name": "C", "parents": ["Y", "G", "Z"]},{"name": "Y", "parents": []},{"name": "D", "parents": []},{"name": "G", "parents": ["Y", "D"]},{"name": "Z", "parents": ["D", "G"]}]'
example = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'

inp = json.loads(example)

tree = {}
tree_res = {}
for d in inp:
    cl = d['name']
    pars = d['parents']
    tree[cl] = pars
    tree_res[cl] = 0


for x in tree.keys():
    for y in tree_res.keys():
        if define(x, y) == 'Yes':
            tree_res[x] += 1

print(tree)
print(tree_res)

res = []

for key,value in tree_res.items():
    res.append(key + ' : ' + str(value))

print(*sorted(res), sep='\n')




