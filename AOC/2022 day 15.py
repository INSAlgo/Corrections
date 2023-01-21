from reader import read

lines = read("day15.txt")

def dist(A, B) :
    return abs(A[0]-B[0]) + abs(A[1]-B[1])

# Part 1 :

xMin, xMax = float('inf'), 0

Y = 2000000

for line in lines :
    s = line[line.index('=')+1:line.index(':')]
    x, y = map(int, s.split(", y="))
    b = line[line.index('=', line.index(':'))+1:]
    bx, by = map(int, b.split(", y="))
    d = dist((x, y), (bx, by))
    yd = abs(y-Y)
    xMin = min(xMin, x - d + yd)
    xMax = max(xMax, x + d - yd)

print(xMin, xMax)

print(xMax - xMin)

# Part 2 :

N = 4000000
places = [[(0, N)] for _ in range(N+1)]

def remove_places(inter: tuple[int], Y: int) :
    r_l, r_r = inter
    i = 0
    while i < len(places[Y]) :
        l, r = places[Y][i]
        if r_l <= l and l <= r_r < r :
            places[Y][i] = (r_r+1, r)
        elif r_l <= l and r <= r_r :
            places[Y].pop(i)
            i -= 1
        elif l < r_l < r and l < r_r < r :
            places[Y][i] = (l, r_l-1)
            i += 1
            places[Y].insert(i, (r_r+1, r))
        elif l < r_l <= r and r <= r_r :
            places[Y][i] = (l, r_l-1)
    
        i += 1

def display() :
    for Y in range(N+1) :
        # print(places[Y])
        if places[Y] :
            line = '#' * (places[Y][0][0])
            for i in range(len(places[Y]) - 1) :
                line += '.' * (places[Y][i][1] - places[Y][i][0] + 1)
                line += '#' * (places[Y][i+1][0] - places[Y][i][1] - 1)
            line += '.' * (places[Y][-1][1] - places[Y][-1][0] + 1)
            line += '#' * (N - places[Y][-1][1])
        else :
            line = '#' * (N+1)
        print(line)
    print()

for line in lines :
    print(line)
    s = line[line.index('=')+1:line.index(':')]
    x, y = map(int, s.split(", y="))
    b = line[line.index('=', line.index(':'))+1:]
    bx, by = map(int, b.split(", y="))
    d = dist((x, y), (bx, by))

    minY, maxY = max(y - d, 0), min(y + d, N)

    for Y in range(minY, maxY+1) :
        dy = abs(Y-y)
        minX, maxX = x - d + dy, x + d - dy
        if minX > N or maxX < 0 :
            continue

        minX, maxX = max(minX, 0), min(maxX, N)
        remove_places((minX, maxX), Y)
    
    # display()

for Y in range(N+1) :
    if len(places[Y]) > 0 :
        print(Y, places[Y])