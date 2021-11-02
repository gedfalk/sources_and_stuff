# Регулярные выражения в Python

'''
Задание "со звёздочкой"
Проверить число, записанной в двоичной СС, на кратность 3 через RegExp

'''

import re
import sys

N = 5000

##pattern = r'0*((1(00)*1)|(10(00)*10(00)*1))0*'
##pattern = r'0*(1(00)*10*|10(00)*1(00)*(11)*0(00)*10*)*0*'  # и даже это неверно
pattern = r'^(0|(1(01*0)*1))*$'

nums_b = [bin(i)[2::] for i in range(N)]
nums_d = [i for i in range(N)]
divide = []

for i in range(N):
    if re.fullmatch(pattern, nums_b[i]):
        divide.append('SUCCESS')
    else:
        divide.append('failed')

    if nums_d[i] % 3 == 0:
        space = ' '
    else:
        space = ''
    print(space, nums_d[i],'\t', space + nums_b[i], '\t', space + divide[i])



'''
for line in sys.stdin:
    line = line.rstrip()
    if re.fullmatch(pattern, line):
        print(line)
'''


'''
Решена, сдана
Понял суть, но разобраться с конструкции смог только на 70%

    Всё сводится к следующему утверждению:
    
    Двоичные числа, делящиеся на 3, делятся на 3 категории:
    
    Числа с двумя последовательными 1 или двумя 1, разделенные четным числом 0. Эффективно каждая пара "отменяет" себя.
    (например, 11, 110, 1100, 1001, 10010, 1111)
    
        (десятичный: 3, 6, 12, 9, 18, 15)
    
    Числа с тремя 1, каждый из которых разделяется нечетным числом 0. Эти триплеты также "отменяют" себя.
    (например, 10101, 101010, 1010001, 1000101)
    
        (десятичный: 21, 42, 81, 69)
    
    Некоторая комбинация первых двух правил (в том числе внутри друг друга)
    (например, 1010111, 1110101, 1011100110001)
    
        (десятичный: 87, 117, 5937)
    
    Таким образом, регулярное выражение, учитывающее эти три правила, просто:
    
        0 * (1 (00) * 10 * | 10 (00) * 1 (00) * (11) * 0 (00) * 10 *) * 0 *

'''