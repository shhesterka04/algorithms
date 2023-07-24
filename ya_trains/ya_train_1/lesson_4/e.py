n = int(input())
d = {}

for i in range(n):
    w, h = [int(x) for x in input().split()]
    if w in d:
        if d[w] < h:
            d[w] = h
    else:
        d[w] = h

ans = 0
for h in d.values():
    ans += h

print(ans)