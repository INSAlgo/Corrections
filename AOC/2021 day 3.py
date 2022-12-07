# https://adventofcode.com/2021/day/3

from collections import Counter


def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    print(lines)
    return lines


def firstProblem(lines: list[str]):
    gammaRate = ""
    epsilonRate = ""
    for i in range(len(lines[0])):
        digit = Counter([line[i] for line in lines]).most_common(1)[0][0]
        gammaRate += digit
        epsilonRate += str(1 - int(digit))
    print(int(gammaRate, 2) * int(epsilonRate, 2))
    return


if __name__ == "__main__":
    lines = read("03input.txt")
    firstProblem(lines)
