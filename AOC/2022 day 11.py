# https://adventofcode.com/2022/day/11

from sys import argv

class Monkey:

    def __init__(self, items, operator, operand, test, iftrue, iffalse) -> None:
        self.items = items
        self.operator = operator
        self.operand = operand
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.count = 0

    def inspect(self, item):
        match self.operator:
            case "+":
                item += self.operand
            case "*":
                item *= self.operand
            case "pow":
                item *= item
        self.count += 1
        return item // 3

    def next(self, item):
        if item % self.test == 0:
            return self.iftrue
        else:
            return self.iffalse

# Provide the input file name as an argument of the python file
with open(argv[1], "r") as file:
    monkeys = []
    while file.readline() != "":
        items = list(map(int, file.readline().strip().split(": ")[1].split(", ")))
        operator, operand = file.readline().strip().split(" = old ")[1].split()
        if "old" in operand:
            operator = "pow"
        else:
            operand = int(operand)
        test = int(file.readline().strip().split(" by ")[1])
        iftrue = int(file.readline().strip().split(" monkey ")[1])
        iffalse = int(file.readline().strip().split(" monkey ")[1])
        file.readline()
        monkeys.append(Monkey(items, operator, operand, test, iftrue, iffalse))

    for i in range(20):
        for monkey in monkeys:
            while len(monkey.items):
                item = monkey.items.pop(0)
                item = monkey.inspect(item)
                next = monkey.next(item)
                monkeys[next].items.append(item)

        print("Round", i+1)
        for j, monkey in enumerate(monkeys):
            print("Monkey", j, ":", *monkey.items)
        print()

    inspections = [monkey.count for monkey in monkeys]
    inspections.sort(reverse=True)
    print(inspections[0]*inspections[1])
