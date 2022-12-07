def make_structure():
    with open('./input.txt') as f:
        lines = f.read().strip().split('\n')
    directories = {'root': {}}
    curr_dir = {}
    path = 'root'
    for line in lines:
        parts = line.split()
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '..':
                    path = path.rsplit('/', 1)[0]
                elif parts[2] == '/':
                    path = 'root'
                else:
                    path += '/' + parts[2]
                    directories[path] = {}
            elif parts[1] == 'ls':
                curr_dir = {}
                directories[path] = curr_dir
                if '/' in path:
                    parent, name = path.rsplit('/', 1)
                    directories[parent][name] = curr_dir
            else:
                raise ValueError(f"Unknown command {parts[1]}")
        else:
            val, name = parts
            if val == 'dir':
                curr_dir[name] = {}
            else:
                if 'files' not in curr_dir:
                    curr_dir['files'] = []
                curr_dir['files'].append(int(val))
    return directories


def calc_dir_size(dir):
    size = 0
    if 'files' in dir:
        size += sum(dir['files'])
    for subdir in dir.values():
        if isinstance(subdir, dict):
            size += calc_dir_size(subdir)
    return size


def part1():
    return sum(
        calc_dir_size(d) for d in make_structure().values()
        if calc_dir_size(d) < 100_000
    )


def part2():
    total = 70_000_000
    desired = 30_000_000
    directories = make_structure()
    to_free = calc_dir_size(directories['root']) - total + desired
    all_dirs_sizes = (calc_dir_size(d) for d in directories.values())
    return min(size for size in all_dirs_sizes if size > to_free)


print("Part 1: ", part1())
print("Part 2: ", part2())