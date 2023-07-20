n = int(input())
arr = [int(x) for x in input().split()]

winner = arr.index(max(arr))
v = -1
points = -1

for i in range(winner + 1, n - 1):
    if arr[i] > arr[i + 1] and arr[i] % 10 == 5 and arr[i] > points:
        v = i
        points = arr[i]

sorted_arr = sorted(arr, reverse=True)
if v == -1:
    print(0)
else:
    print(sorted_arr.index(points) + 1)
