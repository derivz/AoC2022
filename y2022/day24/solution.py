with open('input.txt') as f:
    lines = f.read().strip().split('\n')

directions = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
dir2 = dict(zip(directions.values(), directions.keys()))
n, m = len(lines), len(lines[0])
bliz = {}
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c in directions:
            bliz[(i, j)] = [directions[c]]


def get_next(bliz):
    bliz_next = {}
    for (i, j), dirs in bliz.items():
        for di, dj in dirs:
            toi, toj = i + di, j + dj
            if toi == 0:
                toi = n - 2
            elif toi == n - 1:
                toi = 1
            if toj == 0:
                toj = m - 2
            elif toj == m - 1:
                toj = 1
            bliz_next.setdefault((toi, toj), []).append((di, dj))
    return bliz_next


possible_moves = ((1, 0), (0, 1), (0, 0), (-1, 0), (0, -1))
cur = 0
queue = [(0, 1, 0)]
seen = set()
part1 = part2 = False
while queue:
    y, x, t = queue.pop(0)
    if (y, x, t) in seen:
        continue
    if t == cur:
        bliz = get_next(bliz)
        cur += 1
        seen.clear()
    if y == n - 2 and x == m - 2:
        if not part1:
            part1 = True
            print("Part 1:", t + 1)
            queue.clear()
            queue.append((y + 1, x, t + 1))
            continue
        elif part2:
            print("Part 2:", t + 1)
            break
    if y == 1 and x == 1 and part1 and not part2:
        part2 = True
        queue.clear()
        queue.append((y - 1, x, t + 1))
        print("Part 1.5:", t + 1)
        continue
    for move in possible_moves:
        toy, tox = y + move[0], x + move[1]
        if 0 < toy < n - 1 and 0 < tox < m - 1 and (toy, tox) not in bliz:
            queue.append((toy, tox, t + 1))
        if (tox == 1 and toy == 0) or (tox == m-2 and toy == n-1):
            queue.append((toy, tox, t + 1))
    seen.add((y, x, t))
