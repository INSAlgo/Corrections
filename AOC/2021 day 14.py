# https://adventofcode.com/2021/day/14

from collections import defaultdict,Counter


def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    print(lines)
    return lines


def firstProblem(lines: list[str]):
    insertionDict = defaultdict(str)

    polymer = lines[0]

    for i in range(2,len(lines)):
        pattern,insert=lines[i].split(" -> ")
        insertionDict[pattern]+=insert

    for _ in range(10):
        newPolymer=""

        for letterPos in range(1,len(polymer)):

            insert= polymer[letterPos-1]+insertionDict[polymer[letterPos-1]+polymer[letterPos]]
            newPolymer+=insert
        newPolymer+=polymer[-1]
        polymer=newPolymer

    c=Counter(polymer)
    print(c.most_common()[0][1]-c.most_common()[-1][1])

    return


if __name__ == "__main__":
    lines = read("14input.txt")
    firstProblem(lines)
