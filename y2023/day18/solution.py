with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]
turns = {
    'UU': '|', 'DD': '|', 'LL': '-', 'RR': '-', 'UL': '\\', 'UR': '/',
    'DL': '/', 'DR': '\\', 'LU': '\\', 'LD': '/', 'RU': '/', 'RD': '\\'
}
wall_value = {'-': 0, '|': 1, '\\': -0.5, '/': 0.5}
dirs = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}


# part 2
def color_to_dl(color):
    color = color.strip('(').strip(')').strip('#')
    return 'RDLU'[int(color[-1])], int(color[:-1], 16)


def print_grid2(points, debug=False):
    tot = 0
    allx_segments = []
    ally_segments = []
    px = py = None
    for x in sorted({x for x, y in points if type(x) is int}):
        if px is not None and x - px > 1:
            allx_segments.append((px + 1, x - 1))
        allx_segments.append((x, x))
        px = x
    for y in sorted({y for x, y in points if type(x) is int}):
        if py is not None and y - py > 1:
            ally_segments.append((py + 1, y - 1))
        ally_segments.append((y, y))
        py = y
    # if debug:
    #     for i in range(20):
    #         print(f"{'':9} {'':9}  ", end='')
    #         for x in allx_segments:
    #             print(f"{x[0]:9} {x[1]:9} "[i], end='')
    #         print()
    for y in ally_segments:
        # if debug:
        #     print(f"{y[0]:9} {y[1]:9}  ", end='')
        for x in allx_segments:
            q = is_enclosed2(points, (x[0], y[0]))
            tot += (x[1] - x[0] + 1) * (y[1] - y[0] + 1) if q not in '.' else 0
            if debug:
                print(q, end='')
        if debug:
            print()
    return tot


def is_enclosed2(points, point):
    x, y = point
    right_walls = 0
    if (x, y) in points:
        return points[(x, y)]
    for lp, val in points.items():
        if (
            type(lp[0]) is tuple
            and lp[0][0] <= x <= lp[0][1]
            and lp[1][0] <= y <= lp[1][1]
        ):
            return val
        if type(lp[0]) is int:
            if lp[0] > x and lp[1] == y:
                right_walls += wall_value[val]
        else:
            if x < lp[0][0] and lp[1][0] <= y <= lp[1][1]:
                right_walls += wall_value[val]
    return '#' if right_walls % 2 == 1 else '.'


def solve(p2=False, debug=False):
    s = (0, 0)
    points = {s: None}
    d = sd = None
    for line in lines:
        pd = d
        d, l, color = line.split()
        if p2:
            d, l = color_to_dl(color)
        if sd is None:
            pd = sd = d
        l = int(l)
        points[s] = turns[pd + d]
        end = (s[0] + dirs[d][0] * (l - 1), s[1] + dirs[d][1] * (l - 1))
        points[(
            tuple(sorted((s[0] + dirs[d][0], end[0]))),
            tuple(sorted((s[1] + dirs[d][1], end[1]))),
        )] = turns[d + d]
        s = (end[0] + dirs[d][0], end[1] + dirs[d][1])
    if s == (0, 0):
        points[s] = turns[d + sd]
    return print_grid2(points, debug)


debug = True
print(f"Part 1: {solve(False, debug)}")
print(f"Part 2: {solve(True, debug)}")

