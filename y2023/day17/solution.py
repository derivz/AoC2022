import heapq

with open('input.txt') as f:
    grid = [
        [int(x) for x in line.strip()]
        for line in f.read().split('\n') if line
    ]
    xn, yn = len(grid[0]), len(grid)


def get_shit(p2=False):
    seen = set()
    stack = [(0, 0, 0, 0, (1, 0)), (0, 0, 0, 0, (0, 1))]
    while stack:
        total, x, y, in_a_row, direction = heapq.heappop(stack)
        if (x, y, direction, in_a_row) in seen:
            continue
        seen.add((x, y, direction, in_a_row))
        if x == xn - 1 and y == yn - 1:
            return total
        for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + d[0], y + d[1]
            if (
                not (0 <= nx < xn and 0 <= ny < yn)
                or grid[ny][nx] == 0
                or direction == (-d[0], -d[1])
            ):
                continue
            if not p2 and (d == direction and in_a_row == 3):
                continue
            if p2 and (
                d != direction and in_a_row < 4
                or d == direction and in_a_row >= 10
            ):
                continue
            heapq.heappush(stack, (
                total + grid[ny][nx],
                x + d[0],
                y + d[1],
                in_a_row + 1 if d == direction else 1,
                d
            ))


print("Part 1: ", get_shit())
print("Part 2: ", get_shit(True))
