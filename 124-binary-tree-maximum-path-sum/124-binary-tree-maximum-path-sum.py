# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.mx = -float('inf')
        self.maxSum(root)
        return self.mx
    
    def maxSum(self, root):
        
        if root:
            
            left = max(0, self.maxSum(root.left))
            right = max(0, self.maxSum(root.right))
            
            self.mx = max(self.mx, left + right + root.val)
            
            return max(left, right) + root.val
        
        return 0