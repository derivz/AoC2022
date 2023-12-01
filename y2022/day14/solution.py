with open('input.txt') as f:
    parts = f.read().strip().split('\n')


def print_grid(grid):
    for row in grid:
        print((''.join(map(str, row))).replace('0', '.').replace('1', '#').replace('2', 'O'))


def solution(part2=False):
    start = (500, 0)
    xx = set()
    yy = set()
    for part in parts:
        for c in part.split(' -> '):
            x, y = c.split(',')
            xx.add(int(x))
            yy.add(int(y))

    if part2:
        xx.add(500 + max(yy) + 2)
        xx.add(500 - max(yy) - 2)
        parts.append(f"{500 - max(yy) - 2},{max(yy) + 2} -> "
                     f"{500 + max(yy) + 2},{max(yy) + 2}")

    # since we shrink the grid, we need to adjust the start position with base x
    bx = min(xx) - 1
    grid = [[0] * (max(xx) - min(xx) + 3) for _ in range(max(yy) + 3)]

    for part in parts:
        cc = part.split(' -> ')
        s = cc[0]
        for c in cc[1:]:
            sx, sy = s.split(',')
            x, y = c.split(',')
            s = c
            # deltas to know direction
            dx = (int(x) - int(sx))//abs(int(x) - int(sx)) if int(x) != int(sx) else 1
            dy = (int(y) - int(sy))//abs(int(y) - int(sy)) if int(y) != int(sy) else 1
            for i in range(int(sx), int(x) + dx, dx):
                for j in range(int(sy), int(y) + dy, dy):
                    grid[j][i-bx] = 1

    sand_count = 0
    while True:
        x, y = start
        x -= bx
        if grid[y][x] != 0:
            break
        try:
            while True:
                if grid[y+1][x] == 0:
                    y += 1
                elif grid[y+1][x-1] == 0:
                    y += 1
                    x -= 1
                elif grid[y+1][x+1] == 0:
                    y += 1
                    x += 1
                else:
                    break
            grid[y][x] = 2
            sand_count += 1
        except IndexError:
            # dropping into oblivion
            break

    # print_grid(grid)
    return sand_count


print("Part 1:", solution())

print("Part 2:", solution(part2=True))
