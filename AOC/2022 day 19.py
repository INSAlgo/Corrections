from math import ceil
import sys
from reader import read
from time import time

sys.setrecursionlimit(10000)

lines = read("day19.txt")
N = len(lines)

# Input reading :
types_dict = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}
blueprints: list[dict[int, dict[int, int]]] = []
for line in lines :
    start = line.index(": ") + 2
    parts = line[start:-1].split(". ")
    bp = {}
    for part in parts :
        words = part.split(' ')
        comps = {types_dict[words[5]]: int(words[4])}
        if len(words) > 6 :
            comps[types_dict[words[8]]] = int(words[7])
        bp[types_dict[words[1]]] = comps
    blueprints.append(bp)


# Main rec function :

memo: dict[tuple[int], int] = {}

def solve(turn: int = 1,
    ore: int = 0, clay: int = 0, obsi: int = 0, geode: int = 0,
    ore_bots: int = 1, clay_bots: int = 0, obsi_bots: int = 0, geode_bots: int = 0) :

    # Crash safe :
    if time() - t0 > 1800 :
        print("too slow")
        sys.exit()

    args = (turn, ore, clay, geode, ore_bots, clay_bots, obsi_bots, geode_bots)

    if args in memo :
        return memo[args]

    if turn > N_turns :
        return geode
    rem_turns = N_turns - turn
    res = geode + geode_bots * rem_turns

    materials = [ore, clay, obsi, geode]
    bots = [ore_bots, clay_bots, obsi_bots, geode_bots]

    # print(' '*(turn-1), "turn", turn)
    # print(' '*(turn-1), "bots :", bots)
    # print(' '*(turn-1), "materials :", materials)

    for i in range(3, -1, -1) :
        if bots[i] >= max_bots[i] :
            continue
        wait_turns = -1
        new_mat = materials.copy()
        
        for j, qty in bp[i].items() :
            if materials[j] >= qty :
                wait_turns = max(wait_turns, 0)
                new_mat[j] -= qty
                continue
            if bots[j] == 0 :
                wait_turns = -1
                break
            
            wait = ceil((qty - materials[j])/bots[j])
            wait_turns = max(wait_turns, wait, 0)
            if wait_turns > rem_turns :
                wait_turns = -1
                break
            new_mat[j] -= qty

        if wait_turns < 0 :
            continue

        for j in range(4) :
            new_mat[j] = new_mat[j] + (wait_turns + 1) * bots[j]
        
        new_bots = bots.copy()
        new_bots[i] += 1

        res = max(res, solve(turn + wait_turns + 1, *new_mat, *new_bots))
    
    memo[args] = res
    return res

# Part 1 :

N_turns = 24
i = 1
s = 0
for bp in blueprints :
    max_bots: list[int] = [0, 0, 0, float('inf')]
    for j in range(4) :
        for comp, qty in bp[j].items() :
            max_bots[comp] = max(max_bots[comp], qty)
    memo = {}
    t0 = time()
    res = solve(bp)
    print("bp", i, ":", res)
    s += i * res
    i += 1
print(s)

# Part 2 (too slow) :

N_turns = 32
i = 1
p = 1
for bp in blueprints[:3] :
    max_bots: list[int] = [0, 0, 0, float('inf')]
    for j in range(4) :
        for comp, qty in bp[j].items() :
            max_bots[comp] = max(max_bots[comp], qty)
    memo = {}
    t0 = time()
    res = solve(bp)
    print("bp", i, ":", res)
    p *= res
    i += 1
print(p)