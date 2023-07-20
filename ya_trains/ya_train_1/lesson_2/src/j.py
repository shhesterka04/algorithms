n = int(input())
f_prev = float(input())
f_max = 4000.0
f_min = 30.0
for i in range(n - 1):
    f, status = input().split()
    f = float(f)
    if abs(f - f_prev) < 10 ** (-6):
        continue
    if status == "closer":
        if f < f_prev:
            f_max = min(f_max, (f + f_prev) / 2)
        elif f > f_prev:
            f_min = max(f_min, (f + f_prev) / 2)
    elif status == "further":
        if f < f_prev:
            f_min = max(f_min, (f + f_prev) / 2)
        elif f > f_prev:
            f_max = min(f_max, (f + f_prev) / 2)
    f_prev = f
print("{:.6f} {:.6f}".format(f_min, f_max))
