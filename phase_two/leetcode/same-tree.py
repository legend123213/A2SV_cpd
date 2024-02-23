# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def orderHelper(node,root):
            # if not node or not root:
            #     return True
            if node and root:
                if node.val != root.val:
                    return False
                left = orderHelper(node.left,root.left)
                right = orderHelper(node.right,root.right)
                return left and right
            elif node or root:
                return False
            else:
                return True
            return True
        return orderHelper(p,q)
