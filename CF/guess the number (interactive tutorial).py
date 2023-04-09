# https://codeforces.com/gym/101021/problem/1

from sys import stdout

# this is an example of an interactive problem on codeforces with a simple binary search problem

a, b = 1, 1000001

while b - a > 1 :
    # On every step, a <= x < b

    mid = (a + b) // 2
    
    print(mid)
    stdout.flush()

    res = input()

    if res == '>=' :
        a = mid
    
    elif res == '<' :
        b = mid

print('!', a)