# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ls = []
        def helper(root,res):
            if not root:
                return
            if root.left == None and root.right == None:
                ls.append(str(root.val)+str(res))
                return 
            helper(root.left,str(root.val)+str(res))
            helper(root.right,str(root.val)+str(res))
        helper(root,"")
        result = [int(num[::-1]) for num in ls]
        return sum(result)
        