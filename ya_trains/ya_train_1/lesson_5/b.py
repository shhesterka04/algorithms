n, k  = [int(x) for x in input().split()]
a = list(map(int, input().split()))
ans = 0

preffix = [0] * (n + 1)
for i in range(n):
    preffix[i+1] = preffix[i] + a[i]

countOfPrefixSums = {0: 1}
for i in range(1, n + 1):
    ans += countOfPrefixSums.get(preffix[i] - k, 0)
    countOfPrefixSums[preffix[i]] = countOfPrefixSums.get(preffix[i], 0) + 1

print(ans)
