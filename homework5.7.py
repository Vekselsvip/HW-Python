import random

List = []
for i in range(12):
    List.append(random.randint(7500, 15000))
print(List)
print(sum(List) // len(List))
