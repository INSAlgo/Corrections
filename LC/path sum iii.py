# https://leetcode.com/problems/path-sum-iii/

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        nbOfSolution = [0]
        
        def DFS(node: TreeNode):

            if node is None:
                return []
            
            currentPaths = [node.val]
            if node.val==targetSum:
                nbOfSolution[0]+=1
            

            for childPath in DFS(node.left)+DFS(node.right):
                if node.val+childPath==targetSum:
                    nbOfSolution[0]+=1
                currentPaths.append(node.val+childPath)
            
            return currentPaths

        DFS(root)
        return nbOfSolution[0]
