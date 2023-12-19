with open('input.txt') as f:
    parts = [line.strip() for line in f.read().split('\n\n') if line]

rules = {}
for line in parts[0].split('\n'):
    name, rule = line.split('{')
    rule = rule.strip('}').split(',')
    rr = []
    for r in rule:
        if ':' not in r:
            rr.append(r)
        else:
            wif, wthen = r.split(':')
            k, s, v = wif[0], wif[1], int(wif[2:])
            rr.append((k, s, v, wthen))
    rules[name] = rr


def get_part(p):
    r = {}
    for v in p.strip().strip('{').strip('}').split(','):
        k, v = v.split('=')
        r[k] = int(v)
    return r


def process_workflow(wf, part):
    for wr in wf:
        if not isinstance(wr, tuple):
            return wr
        k, s, v, wthen = wr
        if part[k] > v if s == '>' else part[k] < v:
            return wthen


def get_res(p):
    wf = rules['in']
    while True:
        nxt = process_workflow(wf, p)
        if nxt == 'R':
            return 0
        if nxt == 'A':
            return sum(p.values())
        wf = rules[nxt]


total = 0
for part in parts[1].split('\n'):
    p = get_part(part)
    total += get_res(p)

print(f"Part 1: {total}")

total = 0
rrr = []
stack = [('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000), 0)]
while stack:
    wfn, x, m, a, s, index = stack.pop()
    wf = rules.get(wfn, [wfn])
    for wr in wf[index:]:
        if not isinstance(wr, tuple):
            if wr == 'A':
                total += (
                    (x[1] - x[0] + 1) * (m[1] - m[0] + 1)
                    * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
                )
            elif wr != 'R':
                stack.append((wr, x, m, a, s, 0))
            break
        k, sym, v, wthen = wr
        dd = {'x': x, 'm': m, 'a': a, 's': s}
        kf, ke = dd[k]
        if kf < v <= ke and sym == '<':
            dd[k] = (kf, v - 1)
            stack.append((wthen, dd['x'], dd['m'], dd['a'], dd['s'], 0))
            dd[k] = (v, ke)
            stack.append((wfn, dd['x'], dd['m'], dd['a'], dd['s'], index + 1))
            break
        elif kf <= v < ke and sym == '>':
            dd[k] = (v + 1, ke)
            stack.append((wthen, dd['x'], dd['m'], dd['a'], dd['s'], 0))
            dd[k] = (kf, v)
            stack.append((wfn, dd['x'], dd['m'], dd['a'], dd['s'], index + 1))
            break
        elif ke <= v and sym == '<' or kf > v and sym == '>':
            stack.append((wthen, dd['x'], dd['m'], dd['a'], dd['s'], 0))
            break
        else:
            continue

print(f"Part 2: {total}")
