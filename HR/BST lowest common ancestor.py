# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?isFullScreen=true

# Partie implicite :

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info)

# Partie à coder :

def lca(root: Node, v1, v2):
    currentNode = root
    ma,mi=max(v1,v2),min(v1,v2)
    
    while not(ma>=currentNode.info and mi<=currentNode.info):
        if ma>currentNode.info:
            currentNode=currentNode.right
        else:
            currentNode=currentNode.left
    else:
        return currentNode
