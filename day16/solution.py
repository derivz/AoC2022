from itertools import permutations, combinations

with open('./input.txt') as f:
    lines = f.read().strip().split('\n')

valves = {}
for line in lines:
    valve_name = line.split(' ')[1]
    flow_rate = int(line.split(';')[0].split('=')[1])
    if 'tunnels lead to valves ' in line:
        tunnels = line.split('tunnels lead to valves ')[1].split(', ')
    else:
        tunnels = [line.rsplit(' ', 1)[1]]
    valves[valve_name] = {'flow_rate': flow_rate, 'tunnels': tunnels}

valuable_valves = {v for v in valves if valves[v]['flow_rate'] > 0}
# build the shortest path tree
shortest_paths_next_step = {}
for v, k in valves.items():
    for t in k['tunnels']:
        shortest_paths_next_step[(v, t)] = (t, t, 1)
perfect_scores = {}


def get_next_step(frm, to):
    """Get the shortest route length, along with first step"""
    if (frm, to) in shortest_paths_next_step:
        return shortest_paths_next_step[(frm, to)]
    paths = [(f, f, 1) for f in valves[frm]['tunnels']]
    while True:
        path = paths.pop(0)
        if path[1] == to:
            shortest_paths_next_step[(frm, to)] = path
            return path
        for tun in valves[path[1]]['tunnels']:
            paths.append((path[0], tun, path[2] + 1))


def get_perfect_score(batch, start="AA", time_left=26):
    """Go through all valves to achieve the best possible score

    Kinda does the same that dfp, but much faster
    Only looks at valuable valves, going through them in every possible order
    """
    tb = tuple(batch)
    if (tb, start, time_left) in perfect_scores:
        return perfect_scores[(tb, start, time_left)]
    m = 0
    for v in batch:
        dist = get_next_step(start, v)[2]+1
        if time_left - dist > 0:
            score = (
                    valves[v]['flow_rate'] * (time_left - dist)
                    + get_perfect_score(batch - {v}, v, time_left - dist)
            )
            m = max(m, score)
    perfect_scores[(tb, start, time_left)] = m
    return m


def dfp2_2():
    """Finally manageable solution for part 2

    We divide all valuable valves between two players in every possible way
    Then each one completes its part in the best way possible to have
    the total best of this combination
    """
    maximum = 0
    for first_batch_num in range(7, 0, -1):
        for first_batch in combinations(valuable_valves, first_batch_num):
            total = get_perfect_score(set(first_batch)) + get_perfect_score(
                valuable_valves - set(first_batch))
            if total > maximum:
                maximum = total
    return maximum

# print("Part 1:", dfp('AA'))
print("Part 1:", get_perfect_score(valuable_valves, 'AA', time_left=30))

# print("Part 2:", dfp2('AA', 'AA'))
# print("Part 2:", dfp2_1())
print("FINAL: ", dfp2_2())


###############################################################################
############### ALL previous slow but working solutions below #################
###############################################################################

seen = {}
seen2: dict[(tuple[str, str, tuple, int]) | str, int] = {'max': 0}


def dfp(valve_name, open_valves=tuple(), time_left=30, total=0):
    """Solution for part 1.

    Going through all possible moves at each step
    """
    if (valve_name, open_valves, time_left) in seen:
        return seen[(valve_name, open_valves, time_left)]
    valve = valves[valve_name]
    options = []
    if time_left == 0 or len(open_valves) == len(
            [v for v in valves if valves[v]['flow_rate'] > 0]):
        return total
    if valve['flow_rate'] > 0 and valve_name not in open_valves:
        options.append(dfp(
            valve_name,
            open_valves + (valve_name,),
            time_left - 1,
            total + valve['flow_rate'] * (time_left - 1)
        ))
    for tunnel in valve['tunnels']:
        options.append(dfp(tunnel, open_valves, time_left - 1, total))
    max_value = max(options)
    seen[(valve_name, open_valves, time_left)] = max_value
    return max_value


def dfp2(valve_name1, valve_name2, open_valves=tuple(), time_left=26, total=0):
    """Working solution for part 2.

    Going through all possible moves at each step for both players
    Too sloooooooow despite all memoization and smart stuff
    """
    if (valve_name1, valve_name2, open_valves, time_left) in seen2:
        return seen2[(valve_name1, valve_name2, open_valves, time_left)]
    # halt obviously suboptimal
    max_possible = [valves[v]['flow_rate'] * (time_left - 1) for v in valves if
                    v not in open_valves]
    if total + sum(max_possible) < seen2['max']:
        # seen2[(valve_name1, valve_name2, open_valves, time_left)] = 0
        return 0
    valve1 = valves[valve_name1]
    valve2 = valves[valve_name2]
    options = []
    to_go = valuable_valves - set(open_valves)
    if time_left == 0 or len(to_go) == 0:
        return total
    moves1 = set()
    moves2 = set()
    if valve1['flow_rate'] > 0 and valve_name1 not in open_valves:
        moves1.add((valve_name1, 0))
    if (valve2['flow_rate'] > 0 and valve_name2 not in open_valves
            and valve_name1 != valve_name2):
        moves2.add((valve_name2, 0))
    # chose only valuable valves
    for dest in to_go:
        path1 = get_next_step(valve_name1, dest)
        path2 = get_next_step(valve_name2, dest)
        moves1.add((path1[0], path1[2]))
        moves2.add((path2[0], path2[2]))
        assert path1[0] in valve1['tunnels'], (valve_name1, valve1, path1, dest)
        assert path2[0] in valve2['tunnels'], (valve_name2, valve2, path2, dest)
    # for tunnel in valve1['tunnels']:
    #     moves1.append(tunnel)
    # for tunnel in valve2['tunnels']:
    #     moves2.append(tunnel)
    for move1 in sorted(moves1, key=lambda x: x[1]):
        for move2 in sorted(moves2, key=lambda x: x[1]):
            valve1_dest = move1[0]
            valve2_dest = move2[0]
            new_open_valves = open_valves
            new_total = total
            if valve_name1 == valve1_dest:
                new_open_valves = new_open_valves + (valve_name1,)
                new_total += valve1['flow_rate'] * (time_left - 1)
            if valve_name2 == valve2_dest:
                new_open_valves = new_open_valves + (valve_name2,)
                new_total += valve2['flow_rate'] * (time_left - 1)
            options.append(dfp2(
                valve1_dest, valve2_dest, new_open_valves,
                time_left - 1, new_total
            ))
    max_value = max(options)
    seen2[(valve_name1, valve_name2, open_valves, time_left)] = max_value
    if max_value > seen2['max']:
        seen2['max'] = max_value
    return max_value


def dfp2_1():
    """Working solution for part 2, using permutations

    Only count valuable valves (flow > 0)
    Do all permutations of valuable valves and players start from different
    sides going to the center (this way they split valves between them
    depending on their speed or actually luck).
    Toooo many permutations
    """
    maximum = 0
    i = 0
    for vals in permutations(valuable_valves):
        i += 1
        p1c = p2c = 'AA'
        p1t = p2t = 26
        p1i = 0
        p2i = len(vals) - 1
        total = 0
        p1d = get_next_step(p1c, vals[p1i])[2] + 1
        p2d = get_next_step(p2c, vals[p2i])[2] + 1
        p1t -= p1d
        p2t -= p2d
        while (p1t > 0 or p2t > 0) and p1i <= p2i:
            if p1t >= p2t:
                p1c = vals[p1i]
                p1i += 1
                total += p1t * valves[p1c]['flow_rate']
                p1d = get_next_step(p1c, vals[p1i])[2] + 1
                p1t -= p1d
            else:
                p2c = vals[p2i]
                p2i -= 1
                total += p2t * valves[p2c]['flow_rate']
                p2d = get_next_step(p2c, vals[p2i])[2] + 1
                p2t -= p2d
        if total > maximum:
            maximum = total
    return maximum

