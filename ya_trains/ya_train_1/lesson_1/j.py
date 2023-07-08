from math import gcd

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

deta = a * d - b * c
det1 = e * d - b * f
det2 = a * f - e * c

if deta != 0:
    x = det1 / deta
    y = det2 / deta
    if a == b == 0 and c != 0 and d != 0:
        print(3, round(f / d, 5))
    elif c == d == 0 and a != 0 and b != 0:
        print(4, round(e / b, 5))
    else:
        print(2, round(x, 5), round(y, 5))
else:
    if det1 != det2 != 0:
        print(0)
    else:
        if b == d == 0 and e != 0 and d != 0:
            print(3, round(e / a, 5))
        elif a == c == 0 and b != 0 and  d != 0:
            print(4, round(e / b, 5))
        elif a == b == c == d == e == f == 0:
            print(5)
        else:
            print(1, -gcd(b, d) / gcd(a, c), gcd(e, f) / gcd(a, c))
