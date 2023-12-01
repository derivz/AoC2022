def solution(uniq):
    with open('input.txt') as f:
        line = f.read().strip()
    for i in range(uniq, len(line)+1):
        if len(set(line[i-uniq:i])) == uniq:
            return i


print("Part 1: ", solution(4))
print("Part 1: ", solution(14))
