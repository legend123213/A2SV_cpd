# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nod = ListNode()
        tp = nod
        heada = list1
        headb = list2
        while heada and headb:
            if heada.val >headb.val:
                tp.next = headb
                tp = tp.next
                headb=headb.next
            else:
                tp.next = heada
                tp = tp.next
                heada=heada.next
        while heada:
            tp.next = heada
            tp = tp.next
            heada=heada.next
        while headb:
            tp.next = headb
            tp = tp.next
            headb=headb.next
        return nod.next


        
        