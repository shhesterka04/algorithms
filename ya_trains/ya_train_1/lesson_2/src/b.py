memory = int(input())
num = int(input())
if num == -2000000000:
    print('CONSTANT')
elif num == memory:
    status = 'CONSTANT'
elif num < memory:
    status = 'DESCENDING'
else:
    status = 'ASCENDING'
memory = num
num = int(input())
while num != -2000000000:
    if num == memory:
        if status == 'ASCENDING':
            status = 'WEAKLY ASCENDING'
        elif status == 'DESCENDING':
            status = 'WEAKLY DESCENDING'
    elif num < memory:
        if status == 'CONSTANT':
            status = 'WEAKLY DESCENDING'
        elif status == 'WEAKLY DESCENDING' or status == 'DESCENDING':
            pass
        else:
            status = 'RANDOM'
    elif num > memory:
        if status == 'CONSTANT':
            status = 'WEAKLY ASCENDING'
        elif status == 'WEAKLY ASCENDING' or status == 'ASCENDING':
            pass
        else:
            status = 'RANDOM'

    memory = num
    num = int(input())

print(status)