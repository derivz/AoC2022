with open('./input.txt') as f:
    lines = [line.split() for line in f.read().strip().split('\n')]


def loop(fnc):
    cycles = 0
    x = 1
    for line in lines:
        fnc(cycles, x)
        cycles += 1
        if line[0] == 'addx':
            fnc(cycles, x)
            cycles += 1
            x += int(line[1])


def check(cycle, x):
    global score
    if cycle % 40 == 20:
        score += x * cycle


def paint(cycle, x):
    if abs(x - cycle % 40) < 2:
        image.append('#')
    else:
        image.append('.')


score = 0
loop(check)
print("Part 1:", score)

image = []
loop(paint)
print("Part 2:")
print('\n'.join([''.join(image[i:i + 40]) for i in range(0, len(image), 40)]))
