import sys

words = sys.stdin.read().split()

d = {}

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

maximum = 0

for word in words:
    if d[word] > maximum:
        maximum = d[word]

v = []
for word in words:
    if d[word] == maximum:
        v.append(word)

v = sorted(v)

print(v[0])
