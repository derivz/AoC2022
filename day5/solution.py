def init():
    with open('./input.txt') as f:
        lines = f.read()
    stacks = []
    state, moves = [part.split('\n') for part in lines.split('\n\n')]
    nums_line = state[-1]
    for _ in nums_line.split():
        stacks.append([])
    for line in state[:-1]:
        for i, char in enumerate(line):
            if char not in '[ ]':
                stacks[int(nums_line[i])-1].insert(0, char)
    return stacks, moves


def get_move_numbers(move):
    count, p2 = move.split(' from ')
    frm, to = map(int, p2.split(' to '))
    count = int(count.split(' ')[1])
    return count, frm, to


def part1():
    stacks, moves = init()
    for move in moves:
        if not move:
            continue
        count, frm, to = get_move_numbers(move)
        for i in range(count):
            stacks[to-1].append(stacks[frm-1].pop())

    return ''.join([stack[-1] for stack in stacks if stack])


def part2():
    stacks, moves = init()
    for move in moves:
        if not move:
            continue
        count, frm, to = get_move_numbers(move)
        stacks[to - 1].extend(stacks[frm - 1][-count:])
        stacks[frm - 1][-count:] = []

    return ''.join([stack[-1] for stack in stacks if stack])


print("Part 1: ", part1())

print("Part 2: ", part2())
