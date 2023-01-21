from __future__ import annotations
from copy import deepcopy
from reader import read

lines = read("day11.txt")
init_monkeys: list[Monkey] = []
monkeys: list[Monkey]
nb_monkeys = (len(lines) + 1)//7

part = 1

class Monkey :
    def __init__(
            self, id_: int, objects: list[int], operation: str, value: int,
            criteria: int, if_true: int, if_false: int
        ) -> None:
        self.id = id_
        self.op = operation
        self.val = value
        self.objects = objects
        self.div = criteria
        self.targets = [if_false, if_true]
        self.nb_insp = 0
    
    def inspect(self) :
        N = len(self.objects)

        for i in range(N) :
            if self.op == '+' :
                self.objects[i] += self.val
            elif self.op == '*' :
                self.objects[i] *= self.val
            elif self.op == '²' :
                self.objects[i] **= 2
            else :
                print("wrong operation :", self.op)
            
            if part == 1 :
                self.objects[i] //= 3
            
            self.objects[i] %= mult

        self.nb_insp += N

    def throw(self) :
        for _ in range(len(self.objects)) :
            obj = self.objects.pop()
            monkeys[self.targets[(obj%self.div)==0]].objects.append(obj)
    
    def __lt__(self, other: Monkey) -> bool :
        return self.nb_insp < other.nb_insp
    
    def copy(self) -> Monkey :
        return Monkey(self.id, self.objects, self.op, self.val, self.div, self.targets[1], self.targets[0])

mult = 1
for i in range(nb_monkeys) :
    objects = list(map(int, lines[i*7+1][18:].split(', ')))
    if lines[i*7+2].endswith("* old") :
        oper = '²'
        value = None
    else :
        oper = lines[i*7+2][23]
        value = int(lines[i*7+2][25:])
    div = int(lines[i*7+3][21:])
    if_t = int(lines[i*7+4][29:])
    if_f = int(lines[i*7+5][30:])

    mult *= div

    init_monkeys.append(Monkey(i, objects, oper, value, div, if_t, if_f))

# Part 1 :

monkeys = deepcopy(init_monkeys)
for _ in range(20) :
    for monkey in monkeys :
        monkey.inspect()
        monkey.throw()

monkeys.sort(reverse=True)
print(*[monkey.nb_insp for monkey in monkeys])
print(monkeys[0].nb_insp*monkeys[1].nb_insp)


# Part 2 :
part = 2

monkeys = deepcopy(init_monkeys)
for i in range(10000) :
    # print("iteration ", i)
    for monkey in monkeys :
        # print("monkey", monkey.id, "has", len(monkey.objects), "objects")
        monkey.inspect()
        monkey.throw()

monkeys.sort(reverse=True)
print(*[monkey.nb_insp for monkey in monkeys])
print(monkeys[0].nb_insp*monkeys[1].nb_insp)