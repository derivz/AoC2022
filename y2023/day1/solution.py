import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]

s = 0
for line in lines:
    nums = [x for x in line if x.isdigit()]
    s += int(f'{nums[0]}{nums[-1]}')

print("Part 1: ", s)

numbers = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_num(num):
    return int(numbers.get(num, num))


s2 = 0
for line in lines:
    words = '|'.join(numbers.keys())
    matches = re.findall(f'(?=({words}|\\d))', line)
    s2 += int(f'{get_num(matches[0])}{get_num(matches[-1])}')

print("Part 2: ", s2)
