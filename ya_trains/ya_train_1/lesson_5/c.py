def make_preffix(a, n):
    p = [0] * n
    p[0] = 0
    for i in range(1, n):
        p[i] = p[i - 1]
        if a[i] > a[i - 1]:
            p[i] += a[i] - a[i - 1]

    return p


n = int(input())
a = []
for i in range(n):
    x, y = [int(x) for x in input().split()]
    a.append(y)

preffix = make_preffix(a, n)
reverse_preffix = make_preffix(a[::-1], n)

m = int(input())
for i in range(m):
    s, f = [int(x) for x in input().split()]
    if f > s:
        print(preffix[f - 1] - preffix[s - 1])
    else:
        print(reverse_preffix[n-f]-reverse_preffix[n-s])
