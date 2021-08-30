a = [1, 2, 3, 4]
b = [5, 4, 7, 8]
c = [9, 10, 11, 12]
d = [13, 14, 15, 16]
matrix = a, b, c, d
x = 0
for i in matrix:
    x += len(i)
print(matrix)
print(x)
