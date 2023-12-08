with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]

instructions = lines[0]

rules = {}
for line in lines[1:]:
    frm, to = line.split(' = ')
    tol, tor = to.strip('()').split(', ')
    rules[frm] = (tol, tor)

x = 'AAA'
i = 0
while x != 'ZZZ':
    instruction = instructions[i % len(instructions)]
    x = rules[x][0] if instruction == 'L' else rules[x][1]
    i += 1

print("Part 1: ", i)

zs = []
zxz = {}
for x in rules:
    if x[-1] == 'Z':
        zs.append(x)
for z in zs:
    x = z
    for i in range(len(instructions)):
        j = i
        while True:
            instruction = instructions[j % len(instructions)]
            x = rules[x][0] if instruction == 'L' else rules[x][1]
            j += 1
            if x[-1] == 'Z':
                break

        zxz[(z, i)] = (x, j - i)

xs = []
for x in rules:
    if x[-1] == 'A':
        xs.append(x)

for k, x in enumerate(xs):
    i = 0
    while True:
        instruction = instructions[i % len(instructions)]
        x = rules[x][0] if instruction == 'L' else rules[x][1]
        i += 1
        if x[-1] == 'Z':
            break
    xs[k] = (x, i)

print("Start")
while not all(x[-1] == xs[0][-1] for x in xs):
    m = xs[0][-1] + 1
    mx, mi = None, None
    mj = 0
    for j, x in enumerate(xs):
        if x[-1] < m:
            m = x[-1]
            mx, mi = x
            mj = j
    nmx, nmi = zxz[(mx, mi % len(instructions))]
    xs[mj] = (nmx, mi + nmi)

print("Part 2: ", xs[0][-1])
