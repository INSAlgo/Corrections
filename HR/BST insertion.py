# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem?isFullScreen=true

# Partie implicite :

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

# Partie à coder :

    def insert(self, val):
        if not self.root:
            self.root=Node(val)
            return
        currentNode = self.root
        
        while(1):
            if val<currentNode.info:
                if currentNode.left:
                    currentNode=currentNode.left
                else:
                    currentNode.left = Node(val)
                    break
            else:
                if currentNode.right:
                    currentNode=currentNode.right
                else:
                    currentNode.right = Node(val)
                    break
