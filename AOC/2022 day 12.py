# https://adventofcode.com/2022/day/12

from queue import Queue
from reader import read

lines = read("day12.txt")
h, w = len(lines), len(lines[0])

for i in range(h) :
    if 'E' in lines[i] :
        E = (i, lines[i].index('E'))
    if 'S' in lines[i] :
        S = (i, lines[i].index('S'))

lines[S[0]] = lines[S[0]].replace('S', 'a')
lines[E[0]] = lines[E[0]].replace('E', 'z')

# Part 1 :

def get_next1(pos: tuple[int]) :
    y, x = pos
    N = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
    res = []

    for ny, nx in N :
        if 0 <= nx < w and 0 <= ny < h :
            if ord(lines[ny][nx]) < ord(lines[y][x]) + 2 :
                res.append((ny, nx))
    
    return res

queue = Queue()
queue.put((S, 0))
explored = set()

while queue :
    cur, step = queue.get()
    if cur in explored :
        continue

    if cur == E :
        print(step)
        break
    
    for new in get_next1(cur) :
        queue.put((new, step+1))
    explored.add(cur)

# Part 2 :

def get_next2(pos: tuple[int]) :
    y, x = pos
    N = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
    res = []

    for ny, nx in N :
        if 0 <= nx < w and 0 <= ny < h :
            if ord(lines[ny][nx]) > ord(lines[y][x]) - 2 :
                res.append((ny, nx))
    
    return res

queue = Queue()
queue.put((E, 0))
explored = set()

while queue :
    cur, step = queue.get()
    if cur in explored :
        continue

    if lines[cur[0]][cur[1]] == 'a' :
        print(step)
        break
    
    for new in get_next2(cur) :
        queue.put((new, step+1))
    explored.add(cur)