# Given the sport score sheet. Find second best result

l = [2, 3, 6, 6, 5, 5]

l.sort()
print(list(set(l))[-2])