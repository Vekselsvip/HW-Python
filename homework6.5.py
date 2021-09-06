x = 'iydsi sdfi odsfo idosfo di'
x = x.split()
y = ([len(i) for i in x])
print(y)
print(x[(y.index(max(y)))])