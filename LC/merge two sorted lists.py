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

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val < l2.val:
            return ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
        else:
            return ListNode(l2.val, self.mergeTwoLists(l2.next, l1))           
        
