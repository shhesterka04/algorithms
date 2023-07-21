a = [int(x) for x in input().split()]

s = set()

for el in a:
    s.add(el)

print(len(s))