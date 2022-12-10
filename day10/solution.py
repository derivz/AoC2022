with open('./input.txt') as f:
    lines = [line.split() for line in f.read().strip().split('\n')]

score = 0
x = 1
cycles = 0

to_check = {20, 60, 100, 140, 180, 220}


def check(cycles, x):
    global score
    if cycles in to_check:
        score += x * cycles


for line in lines:
    cycles += 1
    check(cycles, x)
    if line[0] == 'noop':
        pass
    elif line[0] == 'addx':
        x += int(line[1])
        cycles += 1
        check(cycles, x)

print("Part 1:", score)


def paint(cycle, x):
    print(f"Cycle {cycle}: {x}")
    if abs(x - cycles % 40) < 2:
        image.append('#')
    else:
        image.append('.')


cycles = 0
x = 1
image = []
for line in lines:
    paint(cycles, x)
    cycles += 1
    if line[0] == 'noop':
        pass
    elif line[0] == 'addx':
        paint(cycles, x)
        cycles += 1
        x += int(line[1])

print("Part 2:", )

print(image)
parts = [image[i:i + 40] for i in range(0, len(image), 40)]
print('\n'.join(''.join(p) for p in parts))
