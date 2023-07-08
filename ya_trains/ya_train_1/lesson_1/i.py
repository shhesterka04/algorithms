a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


def check_hole(a, b, d, e):
    if (a <= d and b <= e) or (b <= d and a <= e):
        print("YES")
    else:
        print("NO")


max_par = max(a, b, c)
if a == max_par:
    check_hole(c, b, d, e)
elif b == max_par:
    check_hole(a, c, d, e)
else:
    check_hole(a, b, d, e)
