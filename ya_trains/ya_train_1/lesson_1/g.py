n, k, m = map(int, input().split())
details = 0
while n >= k:
    if k < m or n < k:
        break
    prep = n // k
    n = n % k
    details += (k // m) * prep
    n += (k % m) * prep
print(details)



