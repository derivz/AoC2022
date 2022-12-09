with open('./input.txt') as f:
    lines = [line.split() for line in f.read().strip().split('\n')]

rules = {
    'U': (1, 0),
    'D': (-1, 0),
    'R': (0, 1),
    'L': (0, -1)
}


def move(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    if abs(x) * abs(y) > 1:
        b[0] += x // abs(x)
        b[1] += y // abs(y)
    elif abs(x) > 1:
        b[0] += x // abs(x)
    elif abs(y) > 1:
        b[1] += y // abs(y)


def part1():
    h = [0, 0]
    t = [0, 0]
    visited = set()

    for dir, num in lines:
        for _ in range(int(num)):
            x, y = rules[dir]
            h[0] += x
            h[1] += y
            move(h, t)
            visited.add(tuple(t))

    return len(visited)

def part2():
    visited = set()
    rope = [[0,0] for _ in range(10)]

    for dir, num in lines:
        for _ in range(int(num)):
            x, y = rules[dir]
            rope[0][0] += x
            rope[0][1] += y
            for i in range(1, 10):
                move(rope[i-1], rope[i])
            visited.add(tuple(rope[9]))

    return len(visited)


print("Part 1:", part1())
print("Part 2:", part2())
