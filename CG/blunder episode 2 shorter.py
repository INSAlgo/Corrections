# https://www.codingame.com/ide/puzzle/blunder-episode-2

from collections import defaultdict
from functools import cache


n = int(input())
money = defaultdict(int)
previous_rooms = defaultdict(set)
for i in range(n):
    r, m, p1, p2 = input().split()
    money[r] = int(m)
    previous_rooms[p1].add(r)
    previous_rooms[p2].add(r)


@cache
def dp(r):
    if r == "0":
        return money[r]

    return money[r] + max((dp(p) for p in previous_rooms[r]), default=-float("inf"))


print(dp("E"))
