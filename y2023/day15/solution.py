from functools import reduce

with open('input.txt') as f:
    lines = [line for line in f.read().split(',') if line]


def hash(line):
    return reduce(lambda x, y: (x + ord(y)) * 17 % 256, line, 0)


print("Part 1: ", sum(map(hash, lines)))

boxes = [[] for _ in range(256)]
for line in lines:
    label, value = (line.strip('-'), None) if '-' in line else line.split('=')
    box = boxes[hash(label)]
    for i, box_label in enumerate(box):
        if box_label[0] == label:
            if value:
                box[i] = (label, int(value))
            else:
                box.pop(i)
            break
    else:
        if value:
            box.append((label, int(value)))

print("Part 2: ", sum(
    (i + 1) * (j + 1) * (boxes[i][j][1])
    for i in range(len(boxes)) for j in range(len(boxes[i])))
)
