buttons = set([int(x) for x in input().split()])
counter = 0

number = input()
for num in number:
    if int(num) not in buttons:
        counter += 1
        buttons.add(int(num))

print(counter)
