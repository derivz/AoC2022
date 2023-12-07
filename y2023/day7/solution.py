from collections import Counter

with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]


def get_kind(cards, part2=False):
    c = Counter(cards)
    if part2 and "J" in c:
        jc = c["J"]
        if jc == 5:
            return 7
        del c["J"]
        c[c.most_common(1)[0][0]] += jc
    c = c.most_common(2)

    if c[0][-1] == 5:
        return 7
    if c[0][-1] == 4:
        return 6
    if c[0][-1] == 3:
        if c[1][-1] == 2:
            return 5
        return 4
    if c[0][-1] == 2:
        if c[1][-1] == 2:
            return 3
        return 2
    return 1


def make_key(a, part2=False):
    deck = 'J23456789TQKA' if part2 else '23456789TJQKA'
    return get_kind(a[0], part2), *[deck.index(s) for s in a[0]]


hands = [line.split() for line in lines]
result = 0

hands.sort(key=make_key)
for i, hand in enumerate(hands, 1):
    result += i * int(hand[1])

print("Part 1: ", result)

result2 = 0
hands.sort(key=lambda x: make_key(x, True))
for i, hand in enumerate(hands, 1):
    result2 += i * int(hand[1])

print("Part 2: ", result2)
