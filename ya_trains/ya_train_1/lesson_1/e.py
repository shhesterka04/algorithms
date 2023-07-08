def find_flat(k1, k2, k_on_fl):
    # k1 > k2
    delta2 = k1 - k2
    delta_floors = round(delta2/k_on_fl)


k1, m, k2, p2, n2 = map(int, input().split())

delta1 = k2 % n2
k_on_fl = round(n2/delta1)
