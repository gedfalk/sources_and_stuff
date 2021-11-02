
def C(n, k):
	if k > n:
		return 0
	if k == 0:
		return 1
	return(C(n-1, k) + C(n-1, k-1))

n, k  = map(int, input("Введите два числа через пробел: ").split())
print(C(n, k))
