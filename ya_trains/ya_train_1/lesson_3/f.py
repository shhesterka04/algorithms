first = input()
second = input()

pairs = [first[i:i+2] for i in range(len(first)-1)]
counter = 0

pair_dict = {second[i:i+2] for i in range(len(second)-1)}

for pair in pairs:
    if pair in pair_dict:
        counter += 1

print(counter)
