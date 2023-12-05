with open('input.txt') as f:
    groups = [line.strip() for line in f.read().split('\n\n') if line]

seeds = [int(s) for s in groups[0].split(': ')[1].split()]

transformations = []
for group in groups[1:]:
    rules_raw = group.split('\n')[1:]
    rules = []
    for rule in rules_raw:
        dest, src, rng = map(int, rule.split())
        rules.append((src, src + rng, dest))
    transformations.append(rules)


def get_min_seed_location(seeds):
    result = None
    for seed in seeds:
        for rules in transformations:
            for rule in rules:
                src_start, src_end, dest = rule
                if src_start <= seed < src_end:
                    seed = dest + seed - src_start
                    break
        result = min(seed, result) if result else seed
    return result


print("Part 1: ", get_min_seed_location(seeds))

points = set()
for transformation in transformations[-1::-1]:
    new_points = set(points)
    for rule in transformation:
        src_start, src_end, dest = rule
        new_points.add(src_start)
        new_points.add(src_end)
        for point in points:
            if src_start <= point < src_end:
                new_points.add(point - dest + src_start)
    points = new_points

new_seeds = []
for i in range(0, len(seeds), 2):
    new_seeds.append(seeds[i])
    for point in points:
        if seeds[i] <= point < seeds[i] + seeds[i + 1]:
            new_seeds.append(point)

print("Part 2: ", get_min_seed_location(new_seeds))
