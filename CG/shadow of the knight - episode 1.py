# https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.

x, y = [int(i) for i in input().split()]
minx, miny, maxx, maxy = 0, 0, w, h

# game loop
while True:
    d = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if 'R' in d :
        minx = x
        x = (x+maxx)//2
    elif 'L' in d :
        maxx = x
        x = (minx+x)//2
    if 'D' in d :
        miny = y
        y = (y+maxy)//2
    elif 'U' in d :
        maxy = y
        y = (miny+y)//2
    print(x, y)
