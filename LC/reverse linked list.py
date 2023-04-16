# https://leetcode.com/problems/reverse-linked-list/

# Partie implicite :

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Partie à coder :

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        newhead=head
        if head.next:
            newhead= self.reverseList(head.next)
            head.next.next=head
        head.next=None
            
        return newhead