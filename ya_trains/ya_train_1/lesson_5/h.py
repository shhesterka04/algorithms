n, k = [int(x) for x in input().split()]
s = input()
counter = dict()
l = r = 0
max_length = start_index = 0

while r < n:
    counter[s[r]] = counter.get(s[r], 0) + 1

    while any(count > k for count in counter.values()):
        counter[s[l]] -= 1
        if counter[s[l]] == 0:
            del counter[s[l]]
        l += 1

    if r - l + 1 > max_length:
        max_length = r - l + 1
        start_index = l

    r += 1

print(max_length, start_index + 1)
