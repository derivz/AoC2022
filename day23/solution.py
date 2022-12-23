from collections import Counter

with open('./input.txt') as f:
    lines = f.read().strip().split('\n')

elves = {}
for i, line in enumerate(lines):
    for j, s in enumerate(line):
        if s == '#':
            elves[(i, j)] = (i, j)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def make_move(i, elves):
    start_dir = i % len(directions)
    new_elves = {}
    if i == 1:
        pass
    for elf in elves:
        around = [(a, b) for a in range(-1, 2) for b in range(-1, 2) if
                  a != 0 or b != 0]
        if all((elf[0] + p[0], elf[1] + p[1]) not in elves for p in around):
            new_elves[elf] = elf
            continue
        for di in range(4):
            d = directions[(start_dir + di) % 4]
            pos_to_check = [
                (elf[0] + d[0], elf[1] + d[1]),
                (elf[0] + (d[0] or -1), elf[1] + (d[1] or -1)),
                (elf[0] + (d[0] or 1), elf[1] + (d[1] or 1)),
            ]
            if all(p not in elves for p in pos_to_check):
                elves[elf] = pos_to_check[0]
                break
    moves = Counter(elves.values())
    for elf, move in elves.items():
        if moves[move] == 1:
            new_elves[move] = move
        else:
            new_elves[elf] = elf
    return new_elves


for i in range(10):
    elves = make_move(i, elves)

minx = min(elves, key=lambda x: x[1])[1]
miny = min(elves, key=lambda x: x[0])[0]
maxx = max(elves, key=lambda x: x[1])[1]
maxy = max(elves, key=lambda x: x[0])[0]

total = (maxx - minx + 1) * (maxy - miny + 1) - len(elves)
print("Part 1:", total)

elves = {}
for i, line in enumerate(lines):
    for j, s in enumerate(line):
        if s == '#':
            elves[(i, j)] = (i, j)

move_count = 0
while True:
    new_elves = make_move(move_count, elves)
    move_count += 1
    if set(new_elves) == set(elves):
        print("Part 2:", move_count)
        break
    elves = new_elves
