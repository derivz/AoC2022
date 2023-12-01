with open('input.txt') as f:
    lines = f.read().strip().split('\n')

symbols = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
total = sum(symbols[l[-i-1]] * 5 ** i for l in lines for i in range(0, len(l)))
print("Part 1:", total)

revs = {v: k for k, v in symbols.items()}
result = ''
while total:
    total, m = divmod(total, 5)
    if m > 2:
        total += 1
        m -= 5
    result = revs[m] + result
print("Part 2:", result)
