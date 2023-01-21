# https://adventofcode.com/2022/day/18

from reader import read

lines = read("day18.txt")

cubes = []
inf, sup = [float('inf'), float('inf'), float('inf')], [0, 0, 0]

N = len(lines)

for line in lines :
    x, y, z = map(int, line.split(','))
    x += 1
    y += 1
    z += 1
    if x < 1 or y < 1 or z < 1 :
        print(x, y, z)
    cube = (x, y, z)
    cubes.append(cube)
    for i in range(3) :
        inf[i] = min(inf[i], cube[i])
        sup[i] = max(sup[i], cube[i])

space = [[[0 for _ in range(sup[0]+1)] for _ in range(sup[1]+1)] for _ in range(sup[2]+1)]
X, Y, Z = len(space[0][0]), len(space[0]), len(space)

for x, y, z in cubes :
    space[z][y][x] = 1


# for z in range(len(space)) :
#     print(*[''.join(map(str, space[z][y])) for y in range(len(space[z]))], sep='\n')
#     print()

# Part 1 :

s = 0

for z in range(Z) :
    for y in range(Y) :
        for x in range(X) :
            if space[z][y][x] == 0 :
                continue

            neigs = [
                (x-1, y, z), (x+1, y, z),
                (x, y-1, z), (x, y+1, z),
                (x, y, z-1), (x, y, z+1)
            ]

            for xx, yy, zz in neigs :
                if 0 <= xx < X and \
                   0 <= yy < Y and \
                   0 <= zz < Z :
                    if space[zz][yy][xx] == 0 :
                        s += 1
                else :
                    s += 1

print(s)

# Part 2 :

start = (0, 0, 0)

pile = [start]

while pile :
    x, y, z = pile.pop()
    
    neigs = [
        (z-1, y, x), (z+1, y, x),
        (z, y-1, x), (z, y+1, x),
        (z, y, x-1), (z, y, x+1)
    ]

    for zz, yy, xx in neigs :
        if 0 <= xx <= sup[0] and 0 <= yy <= sup[1] and 0 <= zz <= sup[2] and space[zz][yy][xx] == 0 :
            pile.append((xx, yy, zz))

    space[z][y][x] = 2

# for z in range(len(space)) :
#     print(*[''.join(map(str, space[z][y])) for y in range(len(space[z]))], sep='\n')
#     print()

s = 0

for z in range(Z) :
    for y in range(Y) :
        for x in range(X) :
            if space[z][y][x] != 1 :
                continue

            neigs = [
                (z-1, y, x), (z+1, y, x),
                (z, y-1, x), (z, y+1, x),
                (z, y, x-1), (z, y, x+1)
            ]

            for zz, yy, xx in neigs :
                if 0 <= xx < X and \
                   0 <= yy < Y and \
                   0 <= zz < Z :
                    if space[zz][yy][xx] == 2 :
                        s += 1
                else :
                    s += 1

print(s)