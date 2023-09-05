n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

best_l = 0
best_r = n


def create_dict(a: list) -> dict:
    d = dict()
    for el in a:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    return d


def add_element(d: dict, element: int, sufficient_count: dict, counter: int):
    if element in d:
        d[element] += 1
    else:
        d[element] = 1

    if element in sufficient_count and d[element] == sufficient_count[element]:
        counter += 1

    return d, counter


def del_element(d: dict, element: int, sufficient_count: dict, counter: int):
    if d[element] > 1:
        d[element] -= 1
    else:
        d.pop(element)

    if element in sufficient_count and d.get(element, 0) < sufficient_count[element]:
        counter -= 1

    return d, counter


types_tree = create_dict([x for x in range(1, k + 1)])
segment = create_dict(a[:k])
sufficient_count = types_tree.copy()
counter = 0

for el in types_tree:
    if segment.get(el, 0) >= types_tree[el]:
        counter += 1

l = 0
r = k - 1

while r < n:
    if counter == len(types_tree):
        if r - l < best_r - best_l:
            best_l, best_r = l, r
        segment, counter = del_element(segment, a[l], sufficient_count, counter)
        l += 1
    else:
        r += 1
        if r < n:
            segment, counter = add_element(segment, a[r], sufficient_count, counter)

print(best_l + 1, best_r + 1)
