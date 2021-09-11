import random


def rdn():
    x = []
    for i in range(random.randint(20, 100)):
        x.append(random.randint(1, 200))
    return x


def num(x, y):
    a = y
    for i in a:
        if i == x:
            return a.index(x)
    else:
        return -1


z = rdn()
print(num(22, z))
