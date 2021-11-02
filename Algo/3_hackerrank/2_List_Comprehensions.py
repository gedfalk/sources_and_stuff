"""
Let's learn about list comprehensions! You are given 
three integers x, y and z representing the dimensions 
of a cuboid along with an integer n. Print a list of 
all possible coordinates given by (i, j, k) on a 3D 
grid where the sum of i + j + k is not equal to n. 
Please use list comprehensions rather than multiple 
loops, as a learning exercise.
"""

x, y, z = 1, 1, 2
n = 3

L = [[i, k, j] for i in range(x+1) for k in range(y+1) for j in range(z+1) if (i + j + k) != n]

L.sort()
print(L)