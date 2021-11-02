# Стандартные методы и функции строк

"""
Найти число вхождений подстроки в строку

"""

s = input()
t = input()

ind = []

for i in range(len(s)):
    try:
        res_ind = s[i::].index(t) + i
        if res_ind not in ind:
            ind.append(res_ind)
    except:
        pass

print(len(ind))