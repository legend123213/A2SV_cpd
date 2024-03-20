# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        fast,length,lists,count,k1=head,0,[],0,0
        while fast:
            length+=1
            fast=fast.next
        k1,rem=length//k,length%k
        fast=head
        for i in range(k):
            lists.append(fast)
            if rem:
                count = k1 + 1
            else:
                count = k1
            while count-1 and fast:
                fast=fast.next
                count-=1
            if fast:
                fast.next,fast=None,fast.next
            if rem:
                rem-=1
        return lists