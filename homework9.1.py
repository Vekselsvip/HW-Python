def maxsi(*a):
    x = 0
    for i in a:
        if i > x:
            x = i
    return x


print(maxsi(1, 2, 3, 6, 5, 4))
