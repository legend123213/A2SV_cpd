# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mover = head
        temp = None
        while mover:
            x = mover.next
            mover.next = temp
            temp = mover
            mover=x
        return temp


        