# Наибольший общий делитель - НОД

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(min(a,b), max(a,b) % min(a,b))

def main():
    a, b = map(int, input("Введите числа, для которых нужно вычислить НОД - Наибольший Общий Делитель^\n").split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()