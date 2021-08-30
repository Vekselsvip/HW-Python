n = int(input('n'))
x = n
while x % 2 != 0:
    print(('*' * x).center(10))
    x -= 2
    if x < 1:
        break
while x < n:
    x += 2
    print(('*' * x).center(10))
