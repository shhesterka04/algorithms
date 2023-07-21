n = int(input())
everybody = set()
anybody = set()
m = int(input())
for _ in range(m):
    lang = input()
    anybody.add(lang)
    everybody.add(lang)

for i in range(n - 1):
    m = int(input())
    stud_lang = set()
    for j in range(m):
        lang = input()
        stud_lang.add(lang)
    everybody = everybody & stud_lang
    anybody = anybody | stud_lang

print(len(everybody))
for el in everybody:
    print(el)

print(len(anybody))
for el in anybody:
    print(el)

