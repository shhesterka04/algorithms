n = int(input())
a = [int(x) for x in input().split()]
a.sort()
cond = []
m = int(input())
for i in range(m):
    b, c = [int(x) for x in input().split()]
    cond.append([b, c])
cond.sort(key=lambda x: [x[1], x[0]])

ans = 0
p = 0

for classroom in a:
    while p < m:
        if classroom <= cond[p][0]:
            ans += cond[p][1]
            break
        else:
            p += 1

print(ans)
