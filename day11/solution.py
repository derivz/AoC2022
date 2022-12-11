with open('./input.txt') as f:
    monkeyLines = f.read().strip().split('\n\n')


class Monkey:
    def __init__(self, line):
        lines = line.split('\n')
        self.index = int(lines[0].split()[1][:-1])
        self.items = [int(i) for i in lines[1][18:].split(', ')]
        self.op = lambda old: eval(lines[2][19:])
        self.divisor = int(lines[3].rsplit(' ', 1)[1])
        self.posMonkey = int(lines[4].rsplit(' ', 1)[1])
        self.negMonkey = int(lines[5].rsplit(' ', 1)[1])
        self.inspections = 0

    def __repr__(self):
        return f'Monkey({self.index}, {self.inspections})'

    def throwItems(self):
        while self.items:
            item = self.items.pop(0)
            item = self.op(item) // 3
            self.inspections += 1
            yield (
                self.posMonkey if item % self.divisor == 0 else self.negMonkey,
                item
            )


monkeys = [Monkey(line) for line in monkeyLines]
for round in range(20):
    print(f"Round {round + 1}")
    for monkey in monkeys:
        for monkeyIndex, item in monkey.throwItems():
            monkeys[monkeyIndex].items.append(item)
    print()


sortedMonkeys = sorted(monkeys, key=lambda monkey: monkey.inspections, reverse=True)
print("Part 1:", sortedMonkeys[0].inspections * sortedMonkeys[1].inspections)

print("Part 2:")
