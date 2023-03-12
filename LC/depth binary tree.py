# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Partie implicite :

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

# Partie à coder :

class Solution:
   
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS récursif
        if root is None :
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
        
