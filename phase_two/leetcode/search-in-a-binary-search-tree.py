# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = None
        def helperRec(root):
            nonlocal res
            if not root:
                return []
            left = helperRec(root.left)
            right =helperRec(root.right)
            if root.val == val:
                res=root
                return res
        helperRec(root)
        return res
        
        