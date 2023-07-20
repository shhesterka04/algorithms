a = [int(x) for x in input().split()]
a_copy = a[:]

n1 = max(a)
a.pop(a.index(n1))
n2 = max(a)
a.pop(a.index(n2))
n3 = max(a)

m1 = min(a_copy)
a_copy.pop(a_copy.index(m1))
m2 = min(a_copy)
a_copy.pop(a_copy.index(m2))
m3 = max(a_copy)

if n1 * n2 * n3 > m1 * m2 * m3:
    print(n1, n2, n3)
else:
    print(m1, m2, m3)


