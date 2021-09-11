def box(a, b):
    i = 0
    while i < a:
        j = 0
        while j < b:
            print('*', end=' ')
            j += 1
        print()
        i += 1
    return 'not bad'


print(box(4,5))
