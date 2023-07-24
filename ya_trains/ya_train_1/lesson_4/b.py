import sys


def count_words(text: str):
    text = text.split()
    d = {}
    ans = []
    for word in text:
        if word in d:
            d[word] += 1
            ans.append(d[word])
        else:
            d[word] = 0
            ans.append(d[word])

    return ans


t = sys.stdin.read()
print(*count_words(t))
