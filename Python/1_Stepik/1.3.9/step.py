
def closest_mod_5(x):
    y = x
    while y % 5 != 0:
        y +=1
    return y
    # return "I don't know :("


x = int(input("Введите число:"))
print(closest_mod_5(x))

