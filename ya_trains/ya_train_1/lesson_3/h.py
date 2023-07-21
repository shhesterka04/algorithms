n = int(input())
cords = dict()
shoots = 0

for i in range(n):
    x, y = [int(x) for x in input().split()]
    if cords.get(x):
        cords[x].add(y)
    else:
        cords[x] = {y}

for key in cords.keys():
    if len(cords[key]) > 0:
        shoots += 1

print(shoots)





