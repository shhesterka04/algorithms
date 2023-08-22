n = int(input())

d = dict()

for _ in range(n):
    s = input()
    if s.lower() not in d:
        d[s.lower()] = set()
    d[s.lower()].add(s)

s = input().split()
mistakes = 0
for word in s:
    if word.lower() in d:
        if word not in d[word.lower()]:
            mistakes += 1
    else:
        counter = 0
        for letter in word:
            if letter.isupper():
                counter += 1
        if counter != 1:
            mistakes += 1

print(mistakes)
