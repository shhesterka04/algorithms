n, m = [int(x) for x in input().split()]
a = set()
b = set()
for i in range(n):
    a.add(int(input()))
for i in range(m):
    b.add(int(input()))

u = a & b
print(len(u))
print(*sorted(list(u)))

u = a - b
print(len(u))
print(*sorted(list(u)))

u = b - a
print(len(u))
print(*sorted(list(u)))

