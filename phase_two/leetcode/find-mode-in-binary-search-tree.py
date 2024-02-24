# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        res = 0
        def rec(root):
            if not root:
                return -1
            left = rec(root.left)
            right = rec(root.right)
            dic[root.val]+=1
            return root
        rec(root)
        ress = []
        res = max(dic.values())
        for key,val in dic.items():
            if val==res:
                ress.append(key)
        return ress

        