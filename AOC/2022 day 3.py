# https://adventofcode.com/2022/day/3

from reader import read

def priority(char: str) :
    if char.islower() :
        return ord(char)-96
    return ord(char)-65+27

lines = read("day3.txt")

# Part 1 :

letters = []

for line in lines :
    n = len(line)
    letters.append((set(line[:n//2]) & set(line[n//2:])).pop())

print(sum([priority(c) for c in letters]))

# Part 2 :

badges = []

for i in range(len(lines)//3) :
    badges.append(set(lines[3*i]) & set(lines[3*i+1]) & set(lines[3*i+2]))

print(sum([priority(badge.pop()) for badge in badges]))