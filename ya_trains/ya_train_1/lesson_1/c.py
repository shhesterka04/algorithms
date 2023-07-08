numbers = [0]*3


def parse_number(number):
    number = number.replace("-", "")
    number = number.replace('+7', '8')
    number = number.replace('(', '')
    number = number.replace(')', '')
    if len(number) != 11:
        number = '8495' + number
    return number


new_number = parse_number(input())

for i in range(3):
    numbers[i] = parse_number(input())

for number in numbers:
    if number != new_number:
        print('NO')
        continue
    print('YES')
