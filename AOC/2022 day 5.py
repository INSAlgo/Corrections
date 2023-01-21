# https://adventofcode.com/2022/day/5

from reader import read
from copy import deepcopy

lines = read("day5.txt")

crates = lines[:8]
lines = lines[10:]

stacks_init = [[] for _ in range(9)]
for line in crates[::-1] :
    for i in range(9) :
        if line[1 + i*4] != ' ' :
            stacks_init[i].append(line[1 + i*4])

# Part 1 :

stacks = deepcopy(stacks_init)
i = 0
for line in lines :
    n, s, e = map(int, line.split(' ')[1::2])
    s, e = s-1, e-1
    for _ in range(n) :
        to_move = stacks[s].pop()
        stacks[e].append(to_move)

print(''.join(pile[-1] for pile in stacks))

# Part 2 :

stacks = deepcopy(stacks_init)
i = 0
for line in lines :
    n, s, e = map(int, line.split(' ')[1::2])
    s, e = s-1, e-1
    to_move = stacks[s][-n:]
    stacks[s] = stacks[s][:-n]
    stacks[e] += to_move

print(''.join(pile[-1] for pile in stacks))