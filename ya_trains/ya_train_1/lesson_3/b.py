a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
print(*sorted(list(a & b)))


