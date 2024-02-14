# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        ptr_f = head
        if not ptr or not ptr.next:
            return None
        while n!=0 and ptr:
            ptr_f = ptr_f.next
            n-=1
        if not ptr_f:
            return head.next
        while ptr_f:
            ptr_f=ptr_f.next
            if not ptr_f:
                break
            ptr=ptr.next
        if ptr.next:
            ptr.next = ptr.next.next
       
        return head