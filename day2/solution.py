with open('./input.txt') as f:
    lines = [line.split() for line in f.read().split('\n') if line]

rules = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3},
}
extra_points = {"X": 1, "Y": 2, "Z": 3}
score = sum([rules[h][m] + extra_points[m] for h, m in lines])

print("Part 1: ", score)

desired_outcome = {"X": 0, "Y": 3, "Z": 6}
score = 0
for his, outcome in lines:
    result = desired_outcome[outcome]
    my_move = [move for move, score in rules[his].items() if score == result][0]
    score += result + extra_points[my_move]
print("Part 2: ", score)
