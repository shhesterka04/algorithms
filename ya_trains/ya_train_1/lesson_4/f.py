import sys

users = {}

data = sys.stdin.read()
for line in data.splitlines():
    user, item, counter = line.split()
    counter = int(counter)
    if user not in users:
        users[user] = {}
    if item not in users[user]:
        users[user][item] = counter
    else:
        users[user][item] += counter

users = dict(sorted(users.items()))

for key, dvalue in users.items():
    print(f"{key}:")
    dvalue = dict(sorted(dvalue.items()))
    for product, counter in dvalue.items():
        print(f"{product} {counter}")
