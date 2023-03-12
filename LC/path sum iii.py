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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int :
        self.target_sum = targetSum
        
        # Appel inital
        return int(self.DFS(root))

    def DFS(self, root: Optional[TreeNode], path: List[int] = []) -> int :
        res = 0

        # Cas d'arrêt (branche vide)
        if root is None :
            return res
        
        # Incrémentation du chemin
        new_path = path + [root.val]

        # Vérification de toutes les sommes qui se terminent sur ce noeud
        s = 0
        for i in range(len(new_path)) :
            s += new_path[-i-1]
            if s == self.target_sum :
                res += 1
        
        # Récursion :
        return res + self.DFS(root.left, new_path) + self.DFS(root.right, new_path)
