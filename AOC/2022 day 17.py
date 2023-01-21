# https://adventofcode.com/2022/day/17

from reader import read

width = 7
N = 5
N_rocks: int = 2022

def overlap(x: int, y: int, w: int, h: int, rock: list[str]) -> bool :
    for i in range(h) :
        yy = y - i
        if yy < 0 and '#' in rock[i] :
            return True

        for j in range(w) :
            xx = x + j

            if rock[i][j] == '#' :
                if (xx < 0 or 6 < xx) :
                    return True
                if yy < len(grid) and grid[yy][xx] == '#' :
                    return True
    return False

def stop(x: int, y: int, w: int, h: int, rock: list[str]) :
    global grid
    for i in range(h-1, -1, -1) :
        yy = y - i
        if yy >= len(grid) :
            grid.append(['.' for _ in range(width)])
        
        for j in range(w) :
            xx = x + j
            
            if rock[i][j] == '#' :
                grid[yy][xx] = rock[i][j]

# Reading input :

lines = read("day17-rocks.txt")

rocks = []
rock = []
for line in lines :
    if line == "" :
        rocks.append(rock)
        rock = []
    else :
        rock.append(line)

jet = read("day17.txt")[0]
J = len(jet)
# print("number of jets :", J)

# Main function :

grid = []

def solve(k: int = 0, cut: bool = False, nb_rocks: int = N_rocks) :
    global prev_rock

    loops = {0: [(0, 0)]} # {move index%J : [(max height, rock number)]}

    for i in range(nb_rocks) :

        rock = rocks[i%N]
        w, h = len(rock[0]), len(rock)
        x, y = 2, len(grid) + 2 + h
        # print(*[''.join(line) for line in grid][::-1], sep='\n')
        # print("new rock starts at :", x, y)

        while True :
            if jet[k%J] == '>' :
                nx = x + 1
            else :
                nx = x - 1

            if not overlap(nx, y, w, h, rock) :
                x = nx
            k += 1
            
            ny = y - 1

            if overlap(x, ny, w, h, rock) :
                stop(x, y, w, h, rock)
                break
            y = ny

        # Part 2 :

        if cut :

            if i%N == N-1 :
                if k%J not in loops :
                    loops[k%J] = []
                loops[k%J].append((len(grid), i))

                if len(loops[k%J]) == 3 :
                    a, b = loops[k%J][-2], loops[k%J][-1]
                    return (k%J, a[0], b[0], a[1], b[1])


# print(*[''.join(line) for line in grid][::-1], sep='\n')

# Part 1 :

N_rocks = 2022
solve()
print("Part 1 :", len(grid))

# Part 2 :

N_rocks = 10**12
grid = []

res = solve(cut=True, nb_rocks=N_rocks)
if res is not None :
    k, h_a, h_b, i_a, i_b = res
    h_delta = h_b-h_a
    nb_delta = i_b-i_a
    nb_rocks_rem = N_rocks - i_b
    nb_loops = nb_rocks_rem // nb_delta

    solve(k=k, cut=False, nb_rocks=nb_rocks_rem%nb_delta-1)
    # The '-1' is mysterious for me...

    print("Part 2 :", len(grid) + nb_loops * h_delta)
else :
    print("error : returned None")