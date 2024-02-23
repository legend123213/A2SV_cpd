# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helperRecursion(root):
            if not root:
                return []
            left = helperRecursion(root.left)
            right = helperRecursion(root.right)
            return left + [root.val] + right
        return helperRecursion(root)[k-1]


        