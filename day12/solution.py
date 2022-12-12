import sys

sys.setrecursionlimit(5000)

with open('./input.txt') as f:
    lines = f.read().strip().split('\n')


def convert(char):
    if char == 'S':
        return 0
    elif char == 'E':
        return 26
    return ord(char) - ord('a')


start, end = (0, 0)
m = len(lines)
n = len(lines[0])
mappy = [list(map(convert, line)) for line in lines]
for i in range(m):
    for j in range(n):
        if lines[i][j] == 'S':
            start = (i, j)
        elif lines[i][j] == 'E':
            end = (i, j)
visited = {end: 0}


def search(node, score):
    prev = sol[node[0]][node[1]]
    if prev is None or score < prev:
        sol[node[0]][node[1]] = score
        for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x, y = node[0] + a, node[1] + b
            if not (0 <= x < m and 0 <= y < n):
                continue
            if mappy[x][y] > mappy[node[0]][node[1]] + 1:
                continue
            search((x, y), score+1)


sol = [[None] * n for _ in range(m)]
search(start, 0)
print(sol)

shortest = sol[end[0]][end[1]]
print("Part 1:", shortest)


# ultra unoptimized brutal solution
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'a':
            sol = [[None] * n for _ in range(m)]
            search((i, j), 0)
            candidate = sol[end[0]][end[1]]
            if candidate and candidate < shortest:
                shortest = candidate

print("Part 2:", shortest)
