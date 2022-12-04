with open('./input.txt') as f:
    lines = f.read().strip().split('\n')

score = 0
for line in lines:
    common = set(line[:len(line) // 2]).intersection(set(line[len(line) // 2:]))
    letter = common.pop()
    score += ord(letter) - (38 if letter.isupper() else 96)

print("Part 1: ", score)

score = 0
chuncks = [lines[i:i + 3] for i in range(0, len(lines), 3)]
for chunck in chuncks:
    common_letter = set(chunck[0]).intersection(*chunck[1:]).pop()
    score += ord(common_letter) - (38 if common_letter.isupper() else 96)

print("Part 2: ", score)
