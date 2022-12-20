with open('./input.txt') as f:
    lines = f.read().strip().split('\n')


def solution(multiplier=1, mix_rounds=1):
    starting_nums = [int(line) * multiplier for line in lines]
    nums = list(enumerate(starting_nums))
    lenn = len(nums)
    zero = (0, 0)

    for _ in range(mix_rounds):
        for i, n in enumerate(starting_nums):
            frm = nums.index((i, n))
            if n == 0:
                zero = (i, n)
            to = (frm + n) % (lenn - 1) or lenn - 1
            el = nums.pop(frm)
            nums.insert(to, el)

    zero_index = nums.index(zero)
    total = 0
    for i in [1000, 2000, 3000]:
        total += nums[(i + zero_index) % lenn][1]
    return total


print("Part 1: ", solution())
print("Part 2: ", solution(811589153, 10))
