k = int(input())
s = input()
counter = 0
ans = 0
for i in range(k, len(s)):
    if s[i] == s[i - k]:
        counter += 1
        ans += counter
    else:
        counter = 0
print(ans)
