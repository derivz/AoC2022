import re

with open('./input.txt') as f:
    lines = f.read().strip().split('\n')


def parse_line(line):
    line_regex = re.compile(
        r'Blueprint (?P<blueprint_numebr>\d+): '
        r'Each ore robot costs (?P<opo>\d+) ore. '
        r'Each clay robot costs (?P<opc>\d+) ore. '
        r'Each obsidian robot costs (?P<opb>\d+) ore and (?P<cpb>\d+) clay. '
        r'Each geode robot costs (?P<opg>\d+) ore and (?P<bpg>\d+) obsidian.'
    )
    match = line_regex.match(line)
    return {k: int(v) for k, v in match.groupdict().items()}


memo = {}


def get_best_geoge_level(
        lineno, o=0, c=0, b=0, g=0, ro=1, rc=0, rb=0, rg=0, step=0, max_step=24,
        greedy_approach=False
):
    step += 1
    if step > max_step:
        return g
    if (lineno, o, c, b, g, ro, rc, rb, rg, step) in memo:
        return memo[(lineno, o, c, b, g, ro, rc, rb, rg, step)]
    bp = blueprints[lineno]
    mo = max(bp['opo'], bp['opc'], bp['opb'], bp['opg'])
    mc = bp['cpb']
    mb = bp['bpg']
    options = []
    if o >= bp['opg'] and b >= bp['bpg']:
        options.append(get_best_geoge_level(
            lineno, o - bp['opg'] + ro, c + rc, b - bp['bpg'] + rb, g + rg,
            ro, rc, rb, rg + 1, step, max_step, greedy_approach
        ))
    else:
        if o >= bp['opb'] and c >= bp['cpb'] and rb < mb:
            options.append(get_best_geoge_level(
                lineno, o - bp['opb'] + ro, c - bp['cpb'] + rc, b + rb, g + rg,
                ro, rc, rb + 1, rg, step, max_step, greedy_approach
            ))
        if o >= bp['opo'] and ro < mo:
            options.append(get_best_geoge_level(
                lineno, o - bp['opo'] + ro, c + rc, b + rb, g + rg,
                        ro + 1, rc, rb, rg, step, max_step, greedy_approach
            ))
        if o >= bp['opc'] and rc < mc:
            options.append(get_best_geoge_level(
                lineno, o - bp['opc'] + ro, c + rc, b + rb, g + rg,
                ro, rc + 1, rb, rg, step, max_step, greedy_approach
            ))
        if not options or not greedy_approach:
            # for greedy approach, we always build robot with enough resources
            options.append(get_best_geoge_level(
                lineno, o + ro, c + rc, b + rb, g + rg, ro, rc, rb, rg,
                step, max_step, greedy_approach
            ))
    res = max(options)
    memo[(lineno, o, c, b, g, ro, rc, rb, rg, step)] = res
    return res


blueprints = [parse_line(line) for line in lines]

total = 0
for i in range(len(blueprints)):
    print(f"{i + 1}", end='=')
    memo = {}
    cur = get_best_geoge_level(i) * (i + 1)
    print(f"{cur}", end=' ')
    total += cur
print()
# full scan is taking quite a while :coffee:
print("Part 1:", total)

total = 1
for i in range(3):
    print(f"{i + 1}", end='=')
    memo = {}
    cur = get_best_geoge_level(i, max_step=32, greedy_approach=True)
    print(f"{cur}", end=' ')
    total *= cur
print()
# full scan could not be completed within reasonable time and resources
# fortunately, greedy approach works well enough to get correct answer
# still takes a while to run :coffee:
print("Part 2:", total)

