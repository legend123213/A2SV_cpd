# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        if head==None:
            return False
        if head==head.next:
            return True
        head = head.next
        while temp != head:
            temp = temp.next
            if head!=None:
                head = head.next
            else:
                return False
            if head!=None:
                head = head.next
            else:
                return False
            if temp == head:
                return True
        else:
            return False
        