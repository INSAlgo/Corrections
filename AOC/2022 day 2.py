from reader import read

lines = read("day2.txt")

op_moves = ['A', 'B', 'C']

# Part 1 :

my_moves = ['X', 'Y', 'Z']

score = 0

for line in lines :
    [op, my] = line.split()
    i_op, i_my = op_moves.index(op), my_moves.index(my)

    if (i_my-1)%3 == i_op :
        score += 6
    elif i_my == i_op :
        score += 3

    score += i_my + 1

print(score)

# Part 2 :

score = 0

for line in lines :
    [op, my] = line.split()
    i_op = op_moves.index(op)

    if my == 'X' :
        i_my = (i_op-1)%3
    elif my == 'Y' :
        i_my = i_op
        score += 3
    else :
        i_my = (i_op+1)%3
        score += 6
    
    score += i_my + 1

print(score)