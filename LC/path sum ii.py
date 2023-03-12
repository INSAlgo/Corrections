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
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        # Cas d'un arbre vide
        if root is None :
            return False
        
        self.target_sum = target_sum
        
        # Appel initial
        return self.DFS(root)

    def DFS(self, root: Optional[TreeNode], sum_: int = 0) :
        # Cas d'arrêt (branche vide)
        if root is None :
            return False

        # Incrémentation de la somme
        new_sum = sum_ + root.val

        # Cas d'arrêt (feuille)
        if root.left is None and root.right is None :
            return new_sum == self.target_sum

        # Récursion
        return self.DFS(root.left, new_sum) or self.DFS(root.right, new_sum)
