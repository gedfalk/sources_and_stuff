# Даётся сортированный список. Реализовать функцию бинарного поиска


def bin_search(l, item):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (high + low) // 2
        if l[mid] == item:
            return (mid+1)
        elif l[mid] > item:
            high = mid-1
        elif l[mid] < item:
            low = mid+1
    return 'Элемента нет в списке'

    
n = int(input('Программа сгенерирует сортированный массив. Введите его размер: '))
k = int(input('Введите шаг массива: '))
l = [i*k for i in range(1, n+1)]

item = int(input('Введите число, которое нужно найти: '))

print(*l)
print(bin_search(l, item))