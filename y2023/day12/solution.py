with open('input.txt') as f:
    lines = [line.strip() for line in f.read().split('\n') if line]


def get_arrs(line, p2=False):
    def check_arr(arr, nums):
        if (arr, tuple(nums)) in cache:
            return cache[(arr, tuple(nums))]
        if not nums:
            return 1 if not '#' in arr else 0
        if not arr:
            return 0
        r = 0
        if arr[0] == '.':
            r = check_arr(arr.strip('.'), nums)
        elif arr[0] == '#':
            try:
                if (
                    all(a in '?#' for a in arr[:nums[0]])
                    and (len(arr) == nums[0] or arr[nums[0]] in '.?')
                ):
                    r = check_arr(arr[nums[0] + 1:], nums[1:])
                else:
                    r = 0
            except IndexError:
                r = 0
        else:
            r1 = check_arr('#' + arr[1:], nums[:])
            r2 = check_arr('.' + arr[1:], nums[:])
            r = r1 + r2
        cache[(arr, tuple(nums))] = r
        return r

    cache = {}
    code, nums = line.split(' ')
    if p2:
        code = '?'.join(code for _ in range(5))
        nums = ','.join(nums for _ in range(5))
    nums = [int(n) for n in nums.split(',')]
    return check_arr(code, nums[:])

print("Part 1: ", sum(get_arrs(line) for line in lines))
print("Part 2: ", sum(get_arrs(line, True) for line in lines))
