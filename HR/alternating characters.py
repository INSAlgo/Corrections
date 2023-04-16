# https://www.hackerrank.com/challenges/alternating-characters/problem

# Avec regex :

import re

def alternatingCharacters(s):
    match = re.findall(r"(A+|B+)",s)
    return(sum(list(map(len,match)))-len(match))