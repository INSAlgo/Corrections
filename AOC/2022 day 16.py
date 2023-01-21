from queue import PriorityQueue

from reader import read

lines = read("day16.txt")


# Reading input :

N = len(lines)
nodes = {}
edges: list[list[str | int]] = [[] for _ in range(N)]
rates = [0 for _ in range(N)]

for i in range(N) :
    line = lines[i]
    nodes[line[6:8]] = i

    rate = int(line[line.index('=') + 1 : line.index(';')])
    rates[i] = rate

    if "valves" in line :
        edges[i] = set(line[line.index("valves") + 7:].split(", "))
    else :
        edges[i] = {line[line.index("valve") + 6:]}

for i in range(N) :
    edges[i] = [nodes[name] for name in edges[i]]
start = nodes["AA"]

# print(rates)

# Transitive closure :

adj = [[1 if i in edges[j] else 0 if i == j else -1 for i in range(N)] for j in range(N)]
# print(*adj, sep='\n')
# print()

for j in range(N) :
    for i in range(N) :
        if adj[i][j] < 0 :
            continue
        for k in range(N) :
            if adj[j][k] < 0 :
                continue

            new_dist = adj[i][j] + adj[j][k]

            if adj[i][k] < 0 :
                adj[i][k] = new_dist
            else :
                adj[i][k] = min(adj[i][k], new_dist)
# print(*adj, sep='\n')
# print()

# Part 1 :

N_turns = 30

# DP :

steps = [[(-1, 0) for _ in range(N)]]
steps[0][nodes["AA"]] = (0, 0)   # (flow rate, used mask)

global_best = 0

for i in range(1, N_turns+1) :
    step = []
    for k in range(N) :
        if rates[k] == 0 :
            step.append((-1, 0))
            continue

        best = -1
        best_mask = 0

        for j in range(N) :
            step_nb = i - adj[j][k] - 1
            if step_nb < 0 or steps[step_nb][j][0] == -1 :
                continue

            cur_rate, used_mask = steps[step_nb][j]
            if ((1 << k) & used_mask) > 0 :
                continue

            cur_rate += (N_turns-i) * rates[k]
            used_mask |= (1 << k)

            if cur_rate > best :
                best = cur_rate
                best_mask = used_mask

        global_best = max(global_best, best)

        step.append((best, best_mask))
    
    steps.append(step)

# print(*steps, sep='\n')
print("Part 1 :", global_best)

# Part 2 :

N_turns = 26

# Let's try the same thing but with one more dimension : the position of the elephant

steps = [[[None for _ in range(N)] for _ in range(N)] for _ in range(N_turns+1)]
mask = sum((1 << v) for v in range(N) if rates[v] == 0)
# Removing valves with flow 0 from potential goals
steps[0][start][start] = (0, mask, 0, 0)   # (flow rate, opened valves mask, end move self, end move elephant)

res = 0

for turn in range(N_turns+1) :
    print("minute :", turn+1)
    for v1 in range(N) :
        for v2 in range(N) :
            if steps[turn][v1][v2] is None :
                continue

            rate, mask, end1, end2 = steps[turn][v1][v2]
            res = max(res, rate)


            if end1 == end2 == turn :
                # In case both you and the elephant are on your goals :

                for nv1 in range(N-1) :
                    if ((1 << nv1) & mask) > 0 :
                        continue

                    new_end1 = turn + adj[v1][nv1] + 1
                    if new_end1 >= N_turns :
                        continue

                    rate1 = (N_turns-new_end1) * rates[nv1]

                    found_nv2 = False
                    for nv2 in range(nv1+1, N) :
                        if ((1 << nv2) & mask) > 0 :
                            continue

                        new_end2 = turn + adj[v2][nv2] + 1
                        if new_end2 >= N_turns :
                            continue

                        found_nv2 = True

                        rate2 = (N_turns-new_end2) * rates[nv2]

                        new_mask = mask + (1 << nv1) + (1 << nv2)
                        new_end = min(new_end1, new_end2)
                        new_rate = rate + rate1 + rate2

                        if steps[new_end][nv1][nv2] is None or new_rate > steps[new_end][nv1][nv2][0] :
                            steps[new_end][nv1][nv2] = (new_rate, new_mask, new_end1, new_end2)
                    
                    if not found_nv2 :
                        max(res, rate + rate1)
                        
            
            else :  # The most likely case : you or the elephant arrived at a valve to open, the other is still moving
                for nv in range(N) :
                    if ((1 << nv) & mask) > 0 :
                        continue

                    if end1 == turn :
                        new_end1, new_end2 = turn + adj[v1][nv] + 1, end2
                        nv1, nv2 = nv, v2
                        rate1, rate2 = (N_turns-new_end1) * rates[nv1], 0
                    else :
                        new_end1, new_end2 = end1, turn + adj[v2][nv] + 1
                        nv1, nv2 = v1, nv
                        rate1, rate2 = 0, (N_turns-new_end2) * rates[nv2]

                    new_mask = mask + (1 << nv)
                    new_end = min(new_end1, new_end2)
                    new_rate = rate + rate1 + rate2

                    if new_end >= N_turns :
                        continue

                    if steps[new_end][nv1][nv2] is None or new_rate > steps[new_end][nv1][nv2][0] :
                        steps[new_end][nv1][nv2] = (new_rate, new_mask, new_end1, new_end2)
    # print(*steps[turn], sep='\n')
    print()

print("Part 2 :", res)