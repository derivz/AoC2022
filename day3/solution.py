with open('./input.txt') as f:
    lines = f.read().strip().split('\n')

score = 0
for line in lines:
    common = set(line[:len(line) // 2]).intersection(set(line[len(line) // 2:]))
    letter = common.pop()
    score += ord(letter) - (38 if letter.isupper() else 96)

print("Part 1: ", score)

score = 0
for i in range(len(lines) // 3):
    common = (
        set(lines[i * 3 + 0])
        .intersection(set(lines[i * 3 + 1]))
        .intersection(set(lines[i * 3 + 2]))
    )
    letter = common.pop()
    score += ord(letter) - (38 if letter.isupper() else 96)

print("Part 2: ", score)
