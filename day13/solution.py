from functools import cmp_to_key

with open('./input.txt') as f:
    parts = f.read().strip().split('\n\n')


def compare(a, b):
    if isinstance(a, list) and isinstance(b, list):
        for (j, k) in zip(a, b):
            c = compare(j, k)
            if c is not None:
                return c
        return None if len(a) == len(b) else len(b) - len(a)
    if not isinstance(a, list) and not isinstance(b, list):
        return None if a == b else b - a
    if isinstance(a, list):
        return compare(a, [b])
    return compare([a], b)


pairs = [tuple(map(eval, part.split('\n'))) for part in parts]
right = []

for i, (a, b) in enumerate(pairs):
    if compare(a, b) and compare(a, b) > 0:
        right.append(i + 1)
print("Part 1:", sum(right))

divisors = ([[2]], [[6]])
pairs += [divisors]
lines = [line for pair in pairs for line in pair]
lines.sort(key=cmp_to_key(compare), reverse=True)
print("Part 2:", (lines.index(divisors[0])+1) * (lines.index(divisors[1])+1))
