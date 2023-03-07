# https://leetcode.com/problems/path-sum-ii/

# Partie implicite :

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Partie à coder :

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def DFS(node: TreeNode,pathSum,currentPath):
            
            if node is None:
                return
            
            if node.left is None and node.right is None:
                if pathSum+node.val==targetSum:
                    solution.append(currentPath+[node.val])
                return
            
            DFS(node.left,pathSum+node.val,currentPath+[node.val])
            DFS(node.right,pathSum+node.val,currentPath+[node.val])
            
        solution = []
        DFS(root,0,[])
        return solution
