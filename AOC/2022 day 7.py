# https://adventofcode.com/2022/day/7

from sys import argv

class File:
    
    def __init__(self, name, parent=None, size = 0) -> None:
        self.name = name
        self.parent = parent
        self.size = size
        self.childs = []

    def getParent(self):
        return self.parent

    def getChild(self, name):
        for child in self.childs:
            if child.name == name:
                return child

    def addChild(self, child):
        self.childs.append(child)

    def calcSmallest(self):
        if self.size != 0:
            return (self.size, 0)
        size = self.size
        total = 0
        for child in self.childs:
            childSize, childTotal = child.calcSmallest()
            size += childSize
            total += childTotal
        if size <= 100000:
            total += size
        return (size, total)

# Provide the input file name as an argument of the python file
with open(argv[1], "r") as file:

    origin = File("")
    root = File("/", origin)
    origin.addChild(root)
    current = origin

    for line in file:
        if "$ cd" in line:
            if ".." in line:
                current = current.getParent()
            else:
                child = line.strip().split(" ")[2]
                current = current.getChild(child)
        elif "$ ls" in line:
            continue
        else:
            size, name = line.strip().split(" ")
            if size == "dir":
                current.addChild(File(name, current))
            else:
                current.addChild(File(name, current, int(size)))

    rootSize, total = root.calcSmallest()
    print(total)
