with open('input.txt') as f:
    lines = [list(map(int, line)) for line in f.read().strip().split('\n')]

n = len(lines)
m = len(lines[0])


def is_visible(a, b):
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = a + i, b + j
        while 0 <= x < m and 0 <= y < n:
            if lines[y][x] >= lines[b][a]:
                break
            x += i
            y += j
        else:
            return True
    return False


def get_score2(a, b):
    score = 1
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = a + i, b + j
        c = 0
        while 0 <= x < m and 0 <= y < n:
            c += 1
            if lines[y][x] >= lines[b][a]:
                break
            x += i
            y += j
        score *= c
    return score


print("Part 1:", sum(is_visible(i, j) for i in range(m) for j in range(n)))
print("Part 2:", max(get_score2(i, j) for i in range(m) for j in range(n)))
