arr = list(map(int, input().split()))
pre = arr[0]
flag = True
for i in range(1, len(arr)):
    if pre < arr[i]:
        pre = arr[i]
    else:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')