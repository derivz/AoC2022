from collections import defaultdict
from itertools import cycle

with open('./input.txt') as f:
    line = f.read().strip()

# line = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

wind = cycle(line)
shapes_list = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 1), (1, 0), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (0, 1), (1, 0), (1, 1)),
]
wind_of_change = {'>': (1, 0), '<': (-1, 0)}


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self

    def __add__(self, other):
        return Coords(self.x + other[0], self.y + other[1])

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y

    def __iter__(self):
        yield self.x
        yield self.y

    def __eq__(self, other):
        return self.x == other[0] and self.y == other[1]

    def __repr__(self):
        return f"C<{self.x}, {self.y}>"


class Figure:
    def __init__(self, coords):
        self.coords = [Coords(*c) for c in coords]

    def __iadd__(self, other):
        for c in self.coords:
            c += other
        return self

    def __add__(self, other):
        return Figure([c + other for c in self.coords])

    def __iter__(self):
        return iter(self.coords)

    def top(self):
        return max(c.y for c in self)

    def __repr__(self):
        print([c for c in self.coords])
        grid = [['.'] * max(c.x + 1 for c in self.coords) for _ in
                range(max(c.y + 1 for c in self.coords))]
        for c in self.coords:
            grid[-1 - c.y][c.x] = '#'
        return '\n'.join(''.join(g) for g in grid)


class NonMovable(Exception):
    pass


class Grid:
    def __init__(self, y=3):
        self.grid = [['.'] * 7 for _ in range(y)]

    def __repr__(self):
        return '\n'.join(
            ''.join(g) for g in reversed(self.grid)) + '\n' + '$' * 8

    def put(self, fig: Figure):
        while len(self.grid) < max(c.y + 1 for c in fig):
            self.grid.append(['.'] * 7)
        for c in fig:
            self.grid[c.y][c.x] = '#'

    def puttable(self, fig: Figure) -> bool:
        for c in fig:
            if c.y >= len(self.grid):
                continue
            if c.x >= 7 or self.grid[c.y][c.x] == '#':
                return False
        return True

    def movable(self, fig: Figure, gust: tuple[int, int]):
        for c in fig + gust:
            if c.y >= len(self.grid):
                continue
            if c.x >= 7 or c.y < 0 or c.x < 0:
                return False
            try:
                e = self.grid[c.y][c.x]
            except IndexError:
                print(c.x, c.y)
                raise
            if self.grid[c.y][c.x] == '#' and c not in fig:
                return False
        return True

    def clear(self, fig: Figure):
        for c in fig:
            self.grid[c.y][c.x] = '.'

    def move(self, fig: Figure, gust: tuple[int, int]):
        if not self.movable(fig, gust):
            raise NonMovable
        self.clear(fig)
        fig += gust
        self.put(fig)


def get_top_after_rocks(
        rocks_count=None,
        step_mod=None,
        count_steps=False,
        step_mod_iteration_to_stop=1,
):
    wind = cycle(line)
    shapes = cycle(shapes_list)
    top = -1
    rocks = 0
    moving = False
    figure = Figure([])
    grid = Grid()
    step = 0
    step_mod_iteration = 0
    while True:
        step += 1
        gust = wind_of_change[next(wind)]
        if not moving:
            figure = Figure(next(shapes))
            figure += (2, top + 4)
            grid.put(figure)
            moving = True
        if grid.movable(figure, gust):
            grid.move(figure, gust)
        if grid.movable(figure, (0, -1)):
            grid.move(figure, (0, -1))
        else:
            moving = False
            top = max(top, figure.top())
            rocks += 1
            if count_steps and rocks % 5 == 0:
                step_to_count[step % len(line)] += 1
            if step_mod is not None:
                if rocks % 5 == 0 and step % len(line) == step_mod:
                    step_mod_iteration += 1
                    if step_mod_iteration == step_mod_iteration_to_stop:
                        return top, rocks
        if rocks_count is not None and rocks >= rocks_count:
            break
    return top + 1, rocks


step_to_count = defaultdict(int)
print("Part 1:", end=' ')
print(get_top_after_rocks(2022, count_steps=True)[0])

print("Part 2:", end=' ')
ROCKS = 1000000000000
# top, _ = get_top_after_rocks(10000, count_steps=True)
# We have repetitive pattern in the middle
# first find steps on which repetitions starts
# then find new rocks and added height per iteration
# count iterations that fill in limit and add start end finish parts

step_mod = sorted(step_to_count.items(), key=lambda x: (-x[1], -x[0]))[0][0]
first_top, first_rocks = get_top_after_rocks(10000, step_mod,
                                             step_mod_iteration_to_stop=1)
second_top, second_rocks = get_top_after_rocks(10000, step_mod,
                                               step_mod_iteration_to_stop=2)
top_per_iteration = second_top - first_top
rocks_per_iteration = second_rocks - first_rocks
excessive_rocks = (ROCKS - first_rocks) % rocks_per_iteration
top_per_excessive_rocks = (
    get_top_after_rocks(second_rocks + excessive_rocks)[0] - second_top
)

print(
    first_top
    + top_per_iteration * ((ROCKS - first_rocks) // rocks_per_iteration)
    + top_per_excessive_rocks
)
