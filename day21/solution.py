from operator import add, mul, sub, floordiv

with open('./input.txt') as f:
    lines = f.read().strip().split('\n')

ops = dict(line.split(': ', 1) for line in lines)
opd = {'+': add, '-': sub, '*': mul, '/': floordiv}
conv_op = {'+': '-', '-': '+', '*': '/', '/': '*'}


def get_val(val='root', part2=False):
    op = ops[val]
    if op.isdigit():
        return int(op)
    a, s, b = op.split(' ', 3)
    if val == 'root' and part2:
        return get_val(a) == get_val(b)
    return opd[s](get_val(a), get_val(b))


def get_expr(val='root'):
    op = ops[val]
    if val == 'humn':
        return 'humn'
    if op.isdigit():
        return int(op)
    a, s, b = op.split(' ', 3)
    a, b = get_expr(a), get_expr(b)
    if isinstance(a, int) and isinstance(b, int):
        return opd[s](a, b)
    return a, s, b


print("Part 1:", get_val())

expr, _, val = get_expr()
if isinstance(expr, int):
    expr, val = val, expr

while isinstance(expr, tuple):
    expr, s, new_val = expr
    same_op = False
    if isinstance(expr, int):
        expr, new_val = new_val, expr
        if s in '-/':
            # for a = b - x => x = b - a. Same op, different order
            same_op = True
    if same_op:
        val = opd[s](new_val, val)
    else:
        # convert op to opposite: for a = x + b => x = a - b
        val = opd[conv_op[s]](val, new_val)

print("Part 2:", val)
ops['humn'] = str(val)
print("Part 2 correct:", get_val(part2=True))
