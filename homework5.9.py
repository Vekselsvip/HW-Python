List = []
for i in range(2, 100):
    y = 2
    while y < i:
        if i % y == 0:
            break
        y += 1
    else:
        List.append(i)
print(List)
