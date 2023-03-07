# https://leetcode.com/problems/path-sum/

# Partie implicite :

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Partie à coder :

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def DFS(node,pathSum):
            
            if node is None:
                return False
            
            if node.left is None and node.right is None:
                if pathSum + node.val == targetSum:
                    return True
                else:
                    return False
            
            return DFS(node.left,pathSum+node.val) or DFS(node.right,pathSum+node.val)
            
            
        return DFS(root,0)
