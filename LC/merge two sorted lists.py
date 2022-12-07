# https://leetcode.com/problems/merge-two-sorted-lists/

# Partie implcite :

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Partie à coder :

class Solution:
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode()
        if(l2==None and l1==None):
            current=None
        elif l1==None :
            current.val=l2.val
            
            current.next=self.mergeTwoLists(l1,l2.next)
        elif (l2==None or l1.val<l2.val):
            current.val=l1.val
            
            current.next=self.mergeTwoLists(l1.next,l2)
        
            
        else:
            current.val=l2.val
            current.next=self.mergeTwoLists(l1,l2.next)
        
            
        return current