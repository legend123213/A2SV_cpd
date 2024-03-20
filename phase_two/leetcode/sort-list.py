# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        ls.sort()
        dum = ListNode()
        temp = dum
        l = 0
        while l< len(ls):
            dum.next = ListNode(val=ls[l])
            dum = dum.next
            l+=1
        return temp.next

        