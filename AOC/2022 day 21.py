# https://adventofcode.com/2022/day/21

from __future__ import annotations
from queue import Queue
from reader import read

lines = read("day21.txt")
N = len(lines)
val_max = 65536

class Monkey :
    def __init__(self, name: str, val: int = None) :
        self.name = name
        self.val = val
        self.func: function = None
        self.args: list[Monkey] = None
    
    def get_val(self) :
        if self.val is None :
            if self.func is None or self.args is None :
                print("error : uninitialized func or args for monkey", self.name)
                return 0
            self.val = self.func(*self.args)
        return self.val

def ADD(a: Monkey, b: Monkey) :
    return a.get_val() + b.get_val()

def SUB(a: Monkey, b: Monkey) :
    return a.get_val() - b.get_val()

def MULT(a: Monkey, b: Monkey) :
    return a.get_val() * b.get_val()

def DIV(a: Monkey, b: Monkey) :
    return a.get_val() / b.get_val()

functions = {"+" : ADD, "-" : SUB, "*" : MULT, "/" : DIV}

monkeys: dict[str, Monkey] = {}

for line in lines :
    name = line.split(' ')[0].strip(':')
    monkeys[name] = Monkey(name)

# Part 1 :

for line in lines :
    words = line.split(' ')
    dest = words[0].strip(':')
    
    if len(words) == 2 :
        arg = words[1]
        if arg.isnumeric() :
            monkeys[dest].val = int(arg)
            continue
        else :
            print("error, yelled vallue not numeric :", line)
            continue
    
    arg = words[1]
    if arg in monkeys :
        monkey1 = monkeys[arg]
    else :
        print("error : missing monkey", arg)
        continue
    
    arg = words[3]
    if arg in monkeys :
        monkey2 = monkeys[arg]
    else :
        print("error : missing monkey", arg)
        continue

    monkeys[dest].func = functions[words[2]]
    monkeys[dest].args = [monkey1, monkey2]
    continue

res = monkeys["root"].get_val()
print(res)

# Part 2 :

root = monkeys["root"]
[par0, par1] = root.args
q = Queue()
q.put((par0, par1.val))
q.put((par1, par0.val))

while not q.empty() :
    cur_m: Monkey
    cur_m, goal = q.get()

    if cur_m.name == "humn" :
        print(goal)
        break

    if cur_m.func is None :
        continue

    [par0, par1] = cur_m.args
    val0, val1 = par0.val, par1.val

    if cur_m.func is ADD :
        goal0, goal1 = goal - val1, goal - val0
    if cur_m.func is SUB :
        goal0, goal1 = goal + val1, val0 - goal
    if cur_m.func is MULT :
        goal0, goal1 = goal / val1, goal / val0
    if cur_m.func is DIV :
        goal0, goal1 = goal * val1, val0 / goal
    
    q.put((par0, goal0))
    q.put((par1, goal1))