n = int(input())
arr = [int(x) for x in input().split()]


if arr == arr[::-1]:
    print(0)
else:
    for i in range(1, n):
        if arr[i:] == arr[i:][::-1]:
            print(i)
            print(*arr[i-1::-1])
            break
