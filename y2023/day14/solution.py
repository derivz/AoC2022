with open('input.txt') as f:
    platform = [list(line.strip()) for line in f.read().split('\n') if line]
n, m = len(platform), len(platform[0])

total = 0
for j in range(m):
    plus = 0
    for i in range(n):
        if platform[i][j] == 'O':
            total += plus + n - i
        elif platform[i][j] == '#':
            plus = 0
        else:
            plus += 1

print("Part 1: ", total)

seen = {}


def round_of_tilt(index=0, skip_cache=False):
    pc = '\n'.join(''.join(line) for line in platform)
    if pc in seen and not skip_cache:
        return seen[pc]
    seen[pc] = index
    # move north
    for j in range(m):
        step = 0
        for i in range(n):
            if platform[i][j] == 'O':
                if step:
                    platform[i - step][j] = 'O'
                    platform[i][j] = '.'
            elif platform[i][j] == '#':
                step = 0
            else:
                step += 1
    # move west
    for i in range(n):
        step = 0
        for j in range(m):
            if platform[i][j] == 'O':
                if step:
                    platform[i][j - step] = 'O'
                    platform[i][j] = '.'
            elif platform[i][j] == '#':
                step = 0
            else:
                step += 1
    # move south
    for j in range(m):
        step = 0
        for i in range(n - 1, -1, -1):
            if platform[i][j] == 'O':
                if step:
                    platform[i + step][j] = 'O'
                    platform[i][j] = '.'
            elif platform[i][j] == '#':
                step = 0
            else:
                step += 1
    # move east
    for i in range(n):
        step = 0
        for j in range(m - 1, -1, -1):
            if platform[i][j] == 'O':
                if step:
                    platform[i][j + step] = 'O'
                    platform[i][j] = '.'
            elif platform[i][j] == '#':
                step = 0
            else:
                step += 1


def calc_north():
    total = 0
    for j in range(m):
        for i in range(n):
            if platform[i][j] == 'O':
                total += n - i
    return total


num = 1_000_000_000
i = 0
skip_cache = False
while i < num:
    x = round_of_tilt(i, skip_cache)
    if x is not None:
        i += (num - i) // (i - x) * (i - x)
        skip_cache = True
    else:
        i += 1
print("Part 2: ", calc_north())
