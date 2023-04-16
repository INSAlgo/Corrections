# https://www.hackerrank.com/challenges/chief-hopper/problem

import math

def chiefHopper(arr):
    enNecc=[0]
    for lastelem in arr[::-1]:
        enNecc.append(math.ceil((lastelem+enNecc[-1])/2))
    print(enNecc)
    return(enNecc[-1])
