with open('input.txt') as f:
    lines = f.read().strip().split('\n')

cubes = {tuple(int(c) for c in line.split(',')) for line in lines}

total = 0
for cube in cubes:
    cube_total = 6
    for x, y, z in [
        (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)
    ]:
        if (cube[0] + x, cube[1] + y, cube[2] + z) in cubes:
            cube_total -= 1
    total += cube_total
print("Part 1:", total)


max_x = max(cube[0] for cube in cubes) + 1
max_y = max(cube[1] for cube in cubes) + 1
max_z = max(cube[2] for cube in cubes) + 1
min_x = min(cube[0] for cube in cubes) - 1
min_y = min(cube[1] for cube in cubes) - 1
min_z = min(cube[2] for cube in cubes) - 1

queue = [(min_x, min_y, min_z)]
open_cubes = set(queue)

while queue:
    cube = queue.pop()
    if (
            cube[0] < min_x or cube[0] > max_x or cube[1] < min_y or
            cube[1] > max_y or cube[2] < min_z or cube[2] > max_z
    ):
        continue
    for x, y, z in [
        (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)
    ]:
        new_cube = (cube[0] + x, cube[1] + y, cube[2] + z)
        if new_cube in cubes:
            continue
        if new_cube not in open_cubes:
            open_cubes.add(new_cube)
            queue.append(new_cube)

total = 0
for cube in cubes:
    cube_total = 6
    for x, y, z in [
        (1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)
    ]:
        new_cube = (cube[0] + x, cube[1] + y, cube[2] + z)
        if new_cube not in open_cubes:
            cube_total -= 1
    total += cube_total

print("Part 2:", total)
