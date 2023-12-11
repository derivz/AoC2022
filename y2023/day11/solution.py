import itertools

with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]


galaxies = []
ocuppied_rows = set()
ocuppied_cols = set()

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#':
            galaxies.append((i, j))
            ocuppied_rows.add(i)
            ocuppied_cols.add(j)

total = 0
total2 = 0
for combination in itertools.combinations(galaxies, 2):
    x, y = combination
    dist = abs(x[0] - y[0]) + abs(x[1] - y[1])
    exp = 0
    exp += len(set(range(min(x[0], y[0]), max(x[0], y[0]))) - ocuppied_rows)
    exp += len(set(range(min(x[1], y[1]), max(x[1], y[1]))) - ocuppied_cols)
    total += dist + exp
    total2 += dist + exp * 999999

print("Part 1: ", total)
print("Part 2: ", total2)
