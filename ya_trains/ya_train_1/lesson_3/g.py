n = int(input())
truth = 0
combs = set()
for i in range(n):
    a, b = map(int, input().split())
    if a + b == (n - 1) and (a, b) not in combs and a >= 0 and b >= 0:
        truth += 1
        combs.add((a, b))

print(truth)

