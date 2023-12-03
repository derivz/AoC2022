from collections import defaultdict

with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]


result = 0
gears = defaultdict(list)

for j in range(len(lines)):
    line = lines[j]
    c = ''
    l = None
    r = None
    for i in range(len(line) + 1):
        if i < len(line) and line[i].isdigit():
            if l is None:
                l = i
            c += line[i]
        elif c:
            r = i
            # check nums logic
            done = False
            for k in range(l-1, r + 1):
                for m in range(j-1, j+2):
                    try:
                        if lines[m][k] != '.' and not lines[m][k].isdigit():
                            done = True
                            if lines[m][k] == '*':
                                gears[(k, m)].append(int(c))
                    except IndexError:
                        pass
            if done:
                result += int(c)
            c = ''
            l = None
            r = None

print("Part 1: ", result)

result2 = 0
print(f'{gears=}')
for k, v in gears.items():
    if len(v) == 2:
        a, b = v
        result2 += a*b

print("Part 2: ", result2)
