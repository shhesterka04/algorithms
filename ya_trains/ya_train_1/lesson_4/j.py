def clear_line(line: str):
    cleared_line = ""
    for el in line:
        if el.isalpha() or el.isdigit() or el == "_":
            cleared_line += el
        else:
            cleared_line += " "
    return cleared_line

def find_first_max(words_dict: dict):
    max_counter = 0
    min_index = 9999999999999999999999
    answer = ""
    for word, arr in words_dict.items():
        index, counter = arr[0], arr[1]
        if counter > max_counter or counter == max_counter and index < min_index:
            max_counter = counter
            answer = word
            min_index = index
    return answer

def is_correct(word: str, isNum: bool, isReg: bool, keywords: set) -> bool:
    if word in keywords:
        return False
    if not isNum and word[0].isdigit():
        return False
    if isNum and word[0].isdigit() and len(word) == 1:
        return False
    return True
        


fin = open('input.txt', 'r')
n, isReg, isNum = fin.readline().strip().split()
n = int(n)
isReg = isReg == 'yes'
isNum = isNum == 'yes'
indeficators = dict()
keywords = set()
index = 0
for _ in range(n):
    word = fin.readline().strip()
    if not isReg:
        word = word.lower()
    keywords.add(word)

for line in fin.readlines():
    line = clear_line(line.strip())
    words = line.split()
    for word in words:
        if not isReg:
            word = word.lower()
        if is_correct(word, isNum, isNum, keywords):
            if word in indeficators:
                # [0] - index [1] - counter
                indeficators[word][1] +=1
            else:
                indeficators[word] = [0,0]
                indeficators[word][1] = 1
                indeficators[word][0] = index
                index += 1
print(find_first_max(indeficators))


