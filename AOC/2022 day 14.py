# https://adventofcode.com/2022/day/14

import numpy as np
from reader import read

def display(grid: np.matrix) :
    grid = grid.tolist()
    for line in grid :
        print(*line)

lines = read("day14.txt")

paths = []
minX, maxX, minY, maxY = 500, 500, 0, 0
for line in lines :
    points = line.split(" -> ")
    path = []
    for point in points :
        X, Y = map(int, point.split(','))
        maxX = max(maxX, X)
        minX = min(minX, X)
        maxY = max(maxY, Y)
        path.append((X, Y))
    
    paths.append(path)

minX -= 1
maxX += 1

# Part 1 :

w, h = maxX-minX+1, maxY-minY+1
grid = np.zeros(shape=(h, w), dtype=str)
grid.fill('.')

for path in paths :
    for i in range(len(path) - 1) :
        xA, yA = path[i]
        xB, yB = path[i+1]
        xA, xB = xA - minX, xB - minX
        xA, xB = min(xA, xB), max(xA, xB)
        yA, yB = min(yA, yB), max(yA, yB)
        
        grid[yA:yB+1, xA:xB+1].fill('#')

start = (500-minX, 0)
grid[0, 500-minX] = '+'

display(grid)

c = 0

while True :
    x, y = start
    while y < maxY :
        y += 1
        
        if grid[y, x] == '.' :
            continue
        elif x > 0 and grid[y, x-1] == '.' :
            x -= 1
            continue
        elif x < w-1 and grid[y, x+1] == '.' :
            x += 1
            continue
    
        grid[y-1, x] = 'O'
        break

    else :
        break

    c += 1

display(grid)
print(c)


# Part 2 :

maxY += 2
minX = min(500-maxY, minX)
maxX = max(500+maxY, maxX)
paths.append([(minX, maxY), (maxX, maxY)])

w, h = maxX-minX+1, maxY-minY+1
grid = np.zeros(shape=(h, w), dtype=str)
grid.fill('.')

for path in paths :
    for i in range(len(path) - 1) :
        xA, yA = path[i]
        xB, yB = path[i+1]
        xA, xB = xA - minX, xB - minX
        xA, xB = min(xA, xB), max(xA, xB)
        yA, yB = min(yA, yB), max(yA, yB)
        
        grid[yA:yB+1, xA:xB+1].fill('#')

start = (500-minX, 0)
grid[0, 500-minX] = '+'

display(grid)

c = 0

while True :
    x, y = start
    blocked = False

    while True :
        y += 1
        
        if grid[y, x] == '.' :
            continue
        elif x > 0 and grid[y, x-1] == '.' :
            x -= 1
            continue
        elif x < w-1 and grid[y, x+1] == '.' :
            x += 1
            continue
    
        if (x, y-1) == start :
            blocked = True
        grid[y-1, x] = 'O'
        break

    c += 1

    if blocked :
        break

display(grid)
print(c)