# https://leetcode.com/problems/find-center-of-star-graph/

# Partie implicite :

from typing import List

# Partie à coder :

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][1] in edges[1]:
            return edges[0][1]
        else:
            return edges[0][0]
