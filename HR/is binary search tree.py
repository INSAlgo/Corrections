# https://www.hackerrank.com/challenges/is-binary-search-tree/problem?isFullScreen=true

# Partie implicite :

class Node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

# Partie à coder :

def getValues(node: Node):
    if not node:
        return []
    values=[node.data]
    return values+getValues(node.right)+getValues(node.left)

def search(root: Node, value):
    currentNode=root
    while currentNode.data!=value:
        if value>currentNode.data:
            currentNode=currentNode.right
        else:
            currentNode=currentNode.left
        if not currentNode:
            return False
    else:
        return True

def check_binary_search_tree_(root: Node):
    values = getValues(root)
    if len(set(values))!=len(values):
        return False
    for value in values:
        if not search(root,value):
            return False
    else:
        return True
