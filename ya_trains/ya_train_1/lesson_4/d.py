n = int(input())

buttons = [] + [int(x) for x in input().split()]
d = {}


for i in range(n):
    d[i] = buttons[i]

m = int(input())
cmd = [int(x) for x in input().split()]
for click in cmd:
    d[click - 1] -= 1

for key in d.keys():
    if d[key] >= 0:
        print('NO')
    else:
        print('YES')
