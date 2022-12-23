import re

with open('./input.txt') as f:
    input = f.read()

terrain, instructions = input.split('\n\n')
terrain = terrain.split('\n')
maxlen = max(len(line) for line in terrain)
terrain = [line.ljust(maxlen) for line in terrain]
instructions = list(re.findall(r'(\d+|L|R)', instructions))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
rotate = lambda d, r: directions[(directions.index(d) + r) % 4]
start = (0, terrain[0].index('.'))
direction = (0, 1)

for instruction in instructions:
    if instruction == 'L':
        direction = rotate(direction, -1)
    elif instruction == 'R':
        direction = rotate(direction, 1)
    else:
        for _ in range(int(instruction)):
            y, x = start
            y = (y + direction[0]) % len(terrain)
            x = (x + direction[1]) % len(terrain[y])
            while terrain[y][x] == ' ':
                y = (y + direction[0]) % len(terrain)
                x = (x + direction[1]) % len(terrain[y])
            if terrain[y][x] == '#':
                break
            start = (y, x)

total = (start[0] + 1) * 1000 + (start[1] + 1) * 4 + directions.index(direction)
print("Part 1:", total)


def ab_to_d(d, a, b):
    if d == (-1, 0):
        return a, b
    if d == (1, 0):
        return -a, -b
    if d == (0, -1):
        return -b, a
    if d == (0, 1):
        return b, -a


def check_movable(y, x):
    return (
        0 <= y < len(terrain) and 0 <= x < len(terrain[y])
        and terrain[y][x] != ' '
    )


def rotate_grid(y, x, d):
    for _ in range(d % 4):
        y, x = x, MULT - 1 - y
    return y, x


start = (0, terrain[0].index('.'))
direction = (0, 1)

possible_turns = [
    (-1, 1, 1, ((0, 1),)),
    (-1, -1, -1, ((0, -1),)),
    (-1, -2, 2, ((0, -1), (0, -2))),
    (-1, 2, 2, ((0, 1), (0, 2))),
    (1, 2, 2, ((1, 0), (1, 1))),
    (1, -2, 2, ((1, 0), (1, -1))),
    (1, 3, -1, ((0, 1), (1, 1), (1, 2))),
    (3, -2, 0, ((0, -1), (1, -1), (2, -1), (2, -2))),
    (3, -2, 0, ((1, 0), (1, -1), (2, -1), (3, -1))),
    (3, 2, 0, ((1, 0), (1, 1), (2, 1), (3, 1))),
    (3, 2, 0, ((0, 1), (1, 1), (2, 1), (2, 2))),
    (3, -1, 1, ((1, 0), (2, 0), (2, -1))),
]
MULT = 50

for instruction in instructions:
    if instruction == 'L':
        direction = rotate(direction, -1)
    elif instruction == 'R':
        direction = rotate(direction, 1)
    else:
        try:
            for _ in range(int(instruction)):
                y, x = start
                y += direction[0]
                x += direction[1]
                rd = direction
                if (
                    not 0 <= y < len(terrain)
                    or not 0 <= x < len(terrain[0])
                    or terrain[y][x] == ' '
                ):
                    for turn in possible_turns:
                        a, b, d, steps = turn
                        check_y, check_x = start
                        all_steps_present = all(check_movable(
                            check_y + ab_to_d(direction, *step)[0] * MULT,
                            check_x + ab_to_d(direction, *step)[1] * MULT
                        ) for step in steps)
                        if not all_steps_present:
                            continue
                        base_y, extra_y = divmod(check_y, MULT)
                        base_x, extra_x = divmod(check_x, MULT)
                        rd = rotate(direction, d)
                        new_y, new_x = rotate_grid(extra_y, extra_x, d)
                        new_y = (new_y + rd[0]) % MULT
                        new_x = (new_x + rd[1]) % MULT
                        check_y = MULT * (
                                base_y + ab_to_d(direction, a, b)[0]) + new_y
                        check_x = MULT * (
                                base_x + ab_to_d(direction, a, b)[1]) + new_x
                        if check_movable(check_y, check_x):
                            y, x = (check_y, check_x)
                            break
                    else:
                        print("\nWARNING!!!!!!"
                              "\nNecessary transiotion is not described "
                              "in possible_turns \n\n"
                              f"position: {start} direction: {direction} \n")
                        raise Exception

                if terrain[y][x] == '#':
                    break
                start = (y, x)
                direction = rd
        except Exception:
            print(y, x, instruction)
            raise

total = (start[0] + 1) * 1000 + (start[1] + 1) * 4 + directions.index(direction)

print("Part 2:", total)
