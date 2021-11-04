# Число Фибоначчи

def fib(n):
    for i in range(2, n+1):
        mas.append(mas[i-1] + mas[i-2])
    return mas[n]

    
n = int(input("Введите число, из которого высчитается число Фибоначчи: "))
mas = [0, 1]
fib(n)

print('Вычисленные числа:', mas)
print('Ваш ответ:', mas[n])



def f(n):
    mas = [0, 1]
    res = []
    for i in range(2, (n+1)*3):
        mas.append(mas[i-1] + mas[i-2])
        if i % 3 == 0:
            res.append(mas[i])

    print(*res, sep=',')