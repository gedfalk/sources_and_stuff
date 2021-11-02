data = {str(i):[0,0] for i in range(1, 12)}

with open('input.txt', 'r') as inp:
    for line in inp:
        cl, name, height = line.split()
        height = int(height)

        data[cl][0] += 1
        data[cl][1] += height

for i in range(1, 12):
    print(i, data[str(i)][1] / data[str(i)][0])