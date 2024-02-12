# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        counter_a = 0
        counter_b = 0
        temp_a =headA
        temp_b = headB
        
        while temp_a:
            temp_a=temp_a.next
            counter_a+=1
        while temp_b:
            temp_b=temp_b.next
            counter_b+=1
        if counter_a>counter_b:
            if headA:
                for i in range(abs(counter_a-counter_b)):
                    headA= headA.next
        elif counter_b>counter_a:
            if headB:
                for i in range(abs(counter_a-counter_b)):
                    headB= headB.next
        if headA == headB:
            return headA
        while headA and headB:
            headA= headA.next
            headB = headB.next
            if headA == headB:
                return headA
        else:
            return None

        