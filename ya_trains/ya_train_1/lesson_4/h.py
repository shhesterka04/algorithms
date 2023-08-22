g, modS = [int(x) for x in input().split()]
w = input()
s = input()

def check_dicts(d1: dict, d2: dict):
    for key in d1.keys():
        if key not in d2:
            return False
        if d2[key] != d1[key]:
            return False
    return True
             

ans = 0

wdict = dict()
sdict = dict()

for letter in w:
    wdict[letter] = wdict.get(letter, 0) + 1

for i in range(g):
    sdict[s[i]] = sdict.get(s[i], 0) + 1

if check_dicts(wdict, sdict):
    ans += 1

for i in range(modS-g):
    sdict[s[i]] -= 1
    sdict[s[i+g]] = sdict.get(s[i+g], 0) + 1
    if check_dicts(wdict, sdict):
        ans += 1
print(ans)