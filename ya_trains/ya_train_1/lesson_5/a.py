n = int(input())
shorts = [int(x) for x in input().split()]

m = int(input())
tshorts = [int(x) for x in input().split()]

pn = pm = 0
best_delta = shorts[pn]-tshorts[pm]
best_short = 0
best_tshort = 0

for i in range(n + m):
    delta = shorts[pn] - tshorts[pm]
    if abs(delta) < abs(best_delta):
        best_delta = delta
        best_short = pn
        best_tshort = pm
    if delta > 0 and pm < m - 1:
        pm += 1
    elif delta < 0 and pn < n - 1:
        pn += 1
print(shorts[best_short], tshorts[best_tshort])
    