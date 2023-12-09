with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]


def get_next_value(line, p2=False):
    lv = []
    nums = [int(x) for x in line.split(' ')]
    while not all([n == 0 for n in nums]):
        lv.append(nums[0] if p2 else nums[-1])
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1] - nums[i]
        nums.pop()
    if p2:
        return sum(-l if i % 2 else l for i, l in enumerate(lv))
    return sum(lv)


print("Part 1: ", sum([get_next_value(line) for line in lines]))

print("Part 2: ", sum([get_next_value(line, True) for line in lines]))
