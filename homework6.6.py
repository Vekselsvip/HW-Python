x = 'smilesmilesmile'
for i in range(1, len(x) // 2):
    y = x[:i]
    if x.count(y) * len(y) == len(x):
        print(y)
        break
else:
    print('Diff words')
