# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        forward = back = head
        while forward and forward.next:
            back=back.next
            forward = forward.next.next
            if forward == back:
                break
        else:
            return None
        test = head
        while forward != test:
            forward=forward.next
            test= test.next
            
        return test