arr = [int(x) for x in input().split()]

n1 = n2 = n3 = float('-inf')
m1 = m2 = m3 = float('inf')

for num in arr:
    if num > n1:
        n1, n2 = num, n1
    elif num > n2:
        n2 = num
    if num < m1:
        m1, m2 = num, m1
    elif num < m2:
        m2 = num

if n1*n2 > m1*m2:
    print(n2, n1)
else:
    print(m1, m2)
