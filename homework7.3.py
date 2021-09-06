x = {}
y = input('str=')
for i in y:
    if x.get(i):
        continue
    else:
        x[i] = y.count(i)
print(x)