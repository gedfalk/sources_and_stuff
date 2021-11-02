# Сортировка выбором. Сложность О(n^2)

def find_smallest(arr):
    sm = arr[0]
    ind = 0
    for i in range(1, len(arr)):
        if arr[i]<sm:
            sm = arr[i]
            ind = i
    return ind 

def selection_sort(arr):
    L = []
    for i in range(len(arr)):
        si = find_smallest(arr)
        L.append(arr[si])
        arr.pop(si)
    return L

L = [6,7,839,2,0,9,3,87,65,62,3,14,43,27,8]

print(*L)
print(*selection_sort(L))