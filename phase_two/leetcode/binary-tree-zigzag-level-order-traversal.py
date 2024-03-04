# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        pipe = deque([root] if root != None else [])
        while pipe:
            cur_level = []
            for i in range(len(pipe)):
                head = pipe.popleft()
                cur_level.append(head.val)
                if head.left:
                    pipe.append(head.left)
                if head.right:
                    pipe.append(head.right)
            res.append(cur_level)
        return [res[r] if r%2==0 else res[r][::-1] for r in range(len(res))]
        