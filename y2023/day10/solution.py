with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]

s = None
for i, line in enumerate(lines):
    if 'S' in line:
        s = (i, line.index('S'))
        break

moves = {
    '-': {(0, 1): (0, 1), (0, -1): (0, -1)},
    '|': {(1, 0): (1, 0), (-1, 0): (-1, 0)},
    'J': {(1, 0): (0, -1), (0, 1): (-1, 0)},
    'L': {(1, 0): (0, 1), (0, -1): (-1, 0)},
    '7': {(0, 1): (1, 0), (-1, 0): (0, -1)},
    'F': {(0, -1): (1, 0), (-1, 0): (0, 1)},
}

loop = []
prev = None
nxt = s
length = 0
while nxt != s or length == 0:
    loop.append(nxt)
    if prev is None:
        # S == `-` in my input, so I skip finding first move programmatically
        step = [0, 1]
    else:
        prev_step = tuple([nxt[0] - prev[0], nxt[1] - prev[1]])
        step = moves[lines[nxt[0]][nxt[1]]][prev_step]
    prev, nxt = nxt, (nxt[0] + step[0], nxt[1] + step[1])
    length += 1

print("Part 1: ", length // 2)

wall_value = {
    '-': 0, '|': 1, 'L': -0.5, 'J': 0.5, '7': -0.5, 'F': 0.5, 'S': 0
}


def is_enclosed(point):
    if point in loop:
        return False
    x, y = point
    if x == 0 or x == len(lines) - 1 or y == 0 or y == len(lines[0]) - 1:
        return False
    right_walls = 0
    for lp in loop:
        if lp[0] == x and lp[1] > y:
            right_walls += wall_value.get(lines[lp[0]][lp[1]])
    return right_walls % 2 == 1


print("Part 2: ", sum(
    is_enclosed((y, x))
    for x in range(len(lines[0]))
    for y in range(len(lines))
))
