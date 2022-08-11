# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.validation(root, -float('inf'), float('inf'))
    
    def validation(self, root, mn, mx):
        
        if root:
            
            if root.val<=mn or root.val>=mx: return False
            
            return self.validation(root.left, mn, root.val) and self.validation(root.right, root.val, mx)
        return True
    