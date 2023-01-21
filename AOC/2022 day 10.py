# https://adventofcode.com/2022/day/10

from reader import read

lines = read("day10.txt")

# Part 1 :

next_c = 20
C = 0
X = 1
res = 0

for line in lines :
    if line == "noop" :
        C += 1
        if C == next_c :
            res += X*C
            next_c += 40
    
    else :
        _, val = line.split(' ')
        val = int(val)

        C += 2
        if C >= next_c :
            res += X*next_c
            next_c += 40
        
        X += val

print(res)

# Part 2 :

if lines[0] == "noop" :
    new_act = (1, 0)
else :
    _, val = lines[0].split(' ')
    new_act = (2, int(val))
i = 1
C = 0
X = 1
res = ["" for _ in range(6)]

while new_act is not None :
    
    if abs(C%40-X) <=1 :
        res[C//40] += '#'
    else :
        res[C//40] += '.'

    C += 1

    if new_act[0] == C :
        X += new_act[1]
        if i >= len(lines) :
            new_act = None
        elif lines[i] == "noop" :
            new_act = (C+1, 0)
        else :
            _, val = lines[i].split(' ')
            new_act = (C+2, int(val))
        i += 1

print(*res, sep='\n')