def comparison(a, b, c, d, min_length, min_width):
    length = max(a, c)
    width = b + d
    if length * width < min_length * min_width:
        min_width = width
        min_length = length
    return min_length, min_width


a, b, c, d = map(int, input().split())
min_length, min_width = 2000, 2000

min_length, min_width = comparison(a, b, c, d, min_length, min_width)
min_length, min_width = comparison(a, b, d, c, min_length, min_width)
min_length, min_width = comparison(b, a, c, d, min_length, min_width)
min_length, min_width = comparison(b, a, d, c, min_length, min_width)

print(min_length, min_width)
