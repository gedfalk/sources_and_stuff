# Дан список чисел и целевое число
# Вывести индексы двух чисел, которые в сумме дают целевое число


list1 = [2, 7, 11, 15]
list2 = [9, 5, 5, 3]
list3 = [2.5, 6.7, 2.2, 1.8]

num1 = 9
num2 = 10
num3 = 8.9

L = list3
N = num3
l = len(L)

for i in range(l-1):
    y = N - L[i]
    tL = L[i+1::]
    if y in tL:
        resL = [i, tL.index(y)+i+1]
        break

print(resL)




