import sys
sys.setrecursionlimit(2000)

with open('input.txt') as f:
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


def search(node, score):
    prev = sol[node[0]][node[1]]
    if prev is None or score < prev:
        sol[node[0]][node[1]] = score
        for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x, y = node[0] + a, node[1] + b
            if not (0 <= x < m and 0 <= y < n):
                continue
            if mappy[x][y] < mappy[node[0]][node[1]] - 1:
                continue
            search((x, y), score + 1)


sol = [[None] * n for _ in range(m)]
search(end, 0)

shortest = sol[start[0]][start[1]]
print("Part 1:", shortest)


for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'a':
            candidate = sol[i][j]
            if candidate and candidate < shortest:
                shortest = candidate

print("Part 2:", shortest)
