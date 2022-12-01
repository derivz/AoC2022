with open('./input.txt') as f:
    cals = [sum(map(int, line.split('\n'))) for line in f.read().split('\n\n')]
    print("Part 1: ", max(cals))
    print("Part 2: ", sum(sorted(cals)[-3:]))
