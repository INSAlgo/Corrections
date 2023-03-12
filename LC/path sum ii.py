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
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        # Cas d'un arbre vide
        if root is None :
            return []
        
        self.target_sum = target_sum
        
        # Appel initial
        return self.DFS(root)

    def DFS(self, root: Optional[TreeNode], sum_: int = 0, path: list[int] = []) :
        # Cas d'arrêt (branche vide)
        if root is None :
            return []

        # Incrémentation de la somme et du chemin
        new_sum = sum_ + root.val
        new_path = path + [root.val]

        # Cas d'arrêt (feuille)
        if root.left is None and root.right is None :
            if new_sum == self.target_sum :
                return [new_path]
            return []

        # Récursion
        return self.DFS(root.left, new_sum, new_path) + self.DFS(root.right, new_sum, new_path)
