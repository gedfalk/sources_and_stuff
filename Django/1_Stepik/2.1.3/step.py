# Нахождение самого короткого префикса из данного списка

L = ['flow', 'flower', 'flight', 'flu', 'flintasmaghory', 'flfafa']
sample = 'fl'

print(L)
L.sort(key = len)
print(L)

sample = L[0]
found = False

while not found:
    found = True
    for word in L:
        if not word.startswith(sample):
            found = False
            sample = sample[:len(sample)-1:]
            break

print(sample) 