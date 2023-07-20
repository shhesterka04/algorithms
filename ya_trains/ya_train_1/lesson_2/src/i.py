n, m, k = [int(x) for x in input().split()]

a = [[0 for i in range(m + 2)] for j in range(n + 2)]

for _ in range(k):
    i, j = [int(x) for x in input().split()]
    a[i][j] = "*"

    if a[i][j + 1] != "*":
        a[i][j + 1] += 1
    if a[i + 1][j + 1] != "*":
        a[i + 1][j + 1] += 1
    if a[i - 1][j] != "*":
        a[i - 1][j] += 1
    if a[i][j - 1] != "*":
        a[i][j - 1] += 1
    if a[i - 1][j - 1] != "*":
        a[i - 1][j - 1] += 1
    if a[i + 1][j - 1] != "*":
        a[i + 1][j - 1] += 1
    if a[i - 1][j + 1] != "*":
        a[i - 1][j + 1] += 1
    if a[i + 1][j] != "*":
        a[i + 1][j] += 1

for i in range(1, n + 1):
    print(*a[i][1:-1])