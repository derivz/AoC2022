with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]

limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

result = 0
result2 = 0
for line in lines:
    game, moves = line.split(': ')
    game_id = int(game.split(' ')[1])
    moves = moves.split('; ')
    valid = True
    new_limits = {k: 1 for k in limits.keys()}
    for move in moves:
        for color_move in move.split(', '):
            num, color = color_move.split(' ')
            new_limits[color] = max(new_limits[color], int(num))
            if int(num) > limits[color]:
                valid = False
    if valid:
        result += game_id
    result2 += new_limits['red'] * new_limits['green'] * new_limits['blue']

print("Part 1: ", result)

print("Part 2: ", result2)
