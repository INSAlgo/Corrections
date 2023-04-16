from __future__ import annotations

class node :
    def __init__(self, val) -> None:
        self.val = val
        self.left: node = None
        self.right: node = None
        self.ht = 0
    
    def __str__(self) -> str:
        return f"{self.val}(BF={self.get_balance()})"
    
    def update_ht(self) :
        if self.left is None :
            left_h = -1
        else :
            left_h = self.left.ht
        
        if self.right is None :
            right_h = -1
        else :
            right_h = self.right.ht
        
        self.ht = max(left_h, right_h) + 1
    
    def get_balance(self) -> int :
        if self.left is None :
            left_h = -1
        else :
            left_h = self.left.ht
        
        if self.right is None :
            right_h = -1
        else :
            right_h = self.right.ht
        
        return left_h - right_h

def insert(root: node, val: int) :

    # INSERTING :
    
    if root is None :
        return node(val)

    if val < root.val :
        root.left = insert(root.left, val)
    
    elif val > root.val :
        root.right = insert(root.right, val)
    
    else :
        return root

    # BALANCING :

    if root.get_balance() > 1 :
        if root.left.get_balance() == -1 :
            # Left Right Case
            nd_3 = root.left
            nd_4 = nd_3.right
            B = nd_4.left

            root.left = nd_4
            nd_4.left = nd_3
            nd_3.right = B

            nd_3.update_ht()
        
        # Left Left Case
        nd_4 = root.left
        C = nd_4.right

        nd_4.right = root
        root.left = C
        root = nd_4

        root.right.update_ht()
    
    elif root.get_balance() < -1 :
        if root.right.get_balance() == 1 :
            # Right Left Case
            nd_5 = root.right
            nd_4 = nd_5.left
            C = nd_4.right

            root.right = nd_4
            nd_4.right = nd_5
            nd_5.left = C

            nd_5.update_ht()
        
        # Right Right Case
        nd_4 = root.right
        B = nd_4.left

        root.right = B
        nd_4.left = root
        root = nd_4

        root.left.update_ht()
    
    root.update_ht()
    return root

def in_order_traversal(root) :
    """Just a (recursive) DFS to get nodes with in-order traversal"""
    
    if root is None :
        return []
    
    return in_order_traversal(root.left) + [root] + in_order_traversal(root.right)

def pre_order_traversal(root) :
    """Just a (recursive) DFS to get nodes with in-order traversal"""
    
    if root is None :
        return []
    
    return [root] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

if __name__ == "__main__" :
    root = None

    N = int(input())

    for val in map(int, input().split()) :
        root = insert(root, val)
    
    root = insert(root, int(input()))
    
    print(*in_order_traversal(root))
    print(*pre_order_traversal(root))