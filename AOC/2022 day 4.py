from reader import read

lines = read("day4.txt")

# Part 1 :

c = 0
for line in lines :
    rg1, rg2 = line.split(',')
    l1, r1 = map(int, rg1.split('-'))
    l2, r2 = map(int, rg2.split('-'))

    if (l1 <= l2 and r1 >= r2) or (l1 >= l2 and r1 <= r2) :
        c += 1

print(c)

# Part 2 :

c = 0
for line in lines :
    rg1, rg2 = line.split(',')
    l1, r1 = map(int, rg1.split('-'))
    l2, r2 = map(int, rg2.split('-'))

    if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2 :
        c += 1

print(c)