with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]

result = 0
for line in lines:
    line = line.split(': ')[1]
    win, my = line.split(' | ')
    wins = len(set(win.split()) & set(my.split()))
    result += wins and 2 ** (wins - 1)

print("Part 1: ", result)

cards = {n + 1: 0 for n in range(len(lines))}
for line in lines:
    card, line = line.split(': ')
    card_num = int(card[5:])
    win, my = line.split(' | ')
    wins = len(set(win.split()) & set(my.split()))
    cards[card_num] += 1
    for i in range(wins):
        cards[card_num + 1 + i] += cards[card_num]

total = sum(cards.values())

print("Part 2: ", total)
