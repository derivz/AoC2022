with open('./input.txt') as f:
    lines = f.read().strip().split('\n')

score = 0
for line in lines:
    elves = sorted(
        (list(map(int, elf.split('-'))) for elf in line.split(',')),
        key=lambda x: (x[0], -x[1])
    )
    score += elves[1][1] <= elves[0][1]

print("Part 1: ", score)

score = 0
for line in lines:
    elves = sorted(list(map(int, elf.split('-'))) for elf in line.split(','))
    score += elves[1][0] <= elves[0][1]

print("Part 2: ", score)
