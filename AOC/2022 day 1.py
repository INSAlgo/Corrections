# https://adventofcode.com/2022/day/1

from reader import read

lines = read("day1.txt")

elves = [0]

for line in lines :
    if line == "" :
        elves.append(0)
    else :
        elves[-1] += int(line)

#Part 1 :
print(max(elves))

#Part 2 :
elves.sort(reverse=True)
print(sum(elves[:3]))