# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nod = ListNode()
        gre = ListNode()
        bef = nod
        aft = gre
        while head:
            if head.val<x:
                bef.next = head
                bef = bef.next
            else:
                aft.next = head
                aft = aft.next
            head = head.next
        aft.next = None
        bef.next = None
        bef.next = gre.next
        return nod.next



        return nod
        
        