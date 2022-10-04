# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        self.res = False
        def f(root,s):
            
            if root == None:
                return False
            
            s += root.val
            left = f(root.left, s)
            right = f(root.right, s)
            
            if not (left or right) and s == targetSum:
                self.res = True
                return True
            s -= root.val
            return True
        
        f(root, 0)
        return self.res