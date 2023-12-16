with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]
xn, yn = len(lines[0]), len(lines)


def count_energized(position, move):
    seen = {}
    stack = [(position, move)]
    while stack:
        position, move = stack.pop()
        x, y = position
        xm, ym = move
        if not 0 <= x < xn or not 0 <= y < yn:
            continue
        if position in seen and move in seen[position]:
            continue
        if position not in seen:
            seen[position] = {move}
        else:
            seen[position].add(move)

        tile = lines[y][x]
        if (
            tile == '.'
            or tile == '|' and xm == 0
            or tile == '-' and ym == 0
        ):
            stack.append(((x + xm, y + ym), move))
        elif tile in '|-':
            stack.append(((x + ym, y + xm), (ym, xm)))
            stack.append(((x - ym, y - xm), (-ym, -xm)))
        elif tile == '\\':
            stack.append(((x + ym, y + xm), (ym, xm)))
        elif tile == '/':
            stack.append(((x - ym, y - xm), (-ym, -xm)))

    return len(seen)


print("Part 1: ", count_energized((0, 0), (1, 0)))

starting_positions = []
for x in range(xn):
    starting_positions.append(((x, 0), (0, 1)))
    starting_positions.append(((x, yn), (0, -1)))
for y in range(yn):
    starting_positions.append(((0, y), (1, 0)))
    starting_positions.append(((xn, y), (-1, 0)))
print("Part 2: ", max(count_energized(*pos) for pos in starting_positions))
