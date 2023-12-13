with open('input.txt') as f:
    patterns = [line.strip() for line in f.read().split('\n\n') if line]


def parse_pattern(pattern, p2=False):
    def parse_horisontal(pattern, p2=False):
        for i in range(1, len(pattern)):
            off = 0
            for j in range(i + 1):
                if i - 1 - j < 0 or i + j >= len(pattern):
                    if not p2 or off == 1:
                        return i
                    break

                if p2:
                    off += sum(
                        pattern[i - 1 - j][k] != pattern[i + j][k]
                        for k in range(len(pattern[0]))
                    )
                    if off > 1:
                        break
                elif pattern[i - 1 - j] != pattern[i + j]:
                    break
            else:
                if not p2 or off == 1:
                    return i

    pattern = pattern.split('\n')
    if lines := parse_horisontal(pattern, p2):
        return lines * 100
    pattern = [''.join(x) for x in zip(*pattern)]
    return parse_horisontal(pattern, p2)


print("Part 1: ", sum(parse_pattern(pattern) for pattern in patterns))
print("Part 2: ", sum(parse_pattern(pattern, True) for pattern in patterns))
