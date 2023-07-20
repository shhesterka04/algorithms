n = int(input())
arr = [int(x) for x in input().split()]
x = int(input())
best_match = arr[0]
delta = abs(best_match-x)
for el in arr:
    if abs(el - x) < delta:
        best_match = el
        delta = abs(el - x)
print(best_match)