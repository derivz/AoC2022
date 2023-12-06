with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]

times, distances = [map(int, line[10:].split()) for line in lines]
result = 1

for time, distance in zip(times, distances):
    total = 0
    for t in range(time):
        if (time - t) * t > distance:
            total += 1
    result *= total

print("Part 1: ", result)
result2 = 0
time, distance = [int(line[10:].replace(' ', '')) for line in lines]

for t in range(time):
    if (time - t) * t > distance:
        result2 += 1

print("Part 2: ", result2)
