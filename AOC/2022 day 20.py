# https://adventofcode.com/2022/day/20

from reader import read
from collections import Counter

# Part 1 :

lines = list(map(int, read("day20.txt")))

N = len(lines)

A = [[lines[i], i] for i in range(N)]
ref = A.copy()

for i in range(N) :
    [val, ind] = ref[i]
    # print("moving", val)
    if val == 0 :
        continue

    goal = ind + val
    if not (0 <= goal <= N) :
        goal = goal % (N - 1)
    
    if goal == 0 :
        goal = N-1
    
    diff = goal - ind
    if diff == 0 :
        continue

    if diff > 0 :
        for j in range(ind, goal) :
            A[j], A[j+1] = A[j+1], A[j]
            A[j][1] -= 1
            A[j+1][1] += 1
    
    elif diff < 0 :
        for j in range(ind, goal, -1) :
            A[j], A[j-1] = A[j-1], A[j]
            A[j][1] += 1
            A[j-1][1] -= 1
    
    # print(' '.join(map(str, [a[0] for a in A])))

res = 0

A = [a[0] for a in A]
start = A.index(0)

for i in range(1, 4) :
    res += A[(start + i*1000)%N]

print(res)

# Part 2 :

lines = list(map(int, read("day20.txt")))
key = 811589153

N = len(lines)

A = [[lines[i] * key, i] for i in range(N)]
ref = A.copy()

for i in range(N*10) :
    [val, ind] = ref[i%N]
    # print("moving", val)
    if val == 0 :
        continue

    goal = ind + val
    if not (0 <= goal <= N) :
        goal = goal % (N - 1)
    
    if goal == 0 :
        goal = N-1
    
    diff = goal - ind
    if diff == 0 :
        continue

    if diff > 0 :
        for j in range(ind, goal) :
            A[j], A[j+1] = A[j+1], A[j]
            A[j][1] -= 1
            A[j+1][1] += 1
    
    elif diff < 0 :
        for j in range(ind, goal, -1) :
            A[j], A[j-1] = A[j-1], A[j]
            A[j][1] += 1
            A[j-1][1] -= 1

res = 0

A = [a[0] for a in A]
start = A.index(0)

for i in range(1, 4) :
    res += A[(start + i*1000)%N]

print(res)