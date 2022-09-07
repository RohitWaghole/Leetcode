# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if root == None:
            return ''
        
        if root.right == None and root.left == None:
            return str(root.val)+''
        
        if root.right == None:
            return str(root.val) + '(' + str(self.tree2str(root.left)) + ')'
        
        return str(root.val) + '(' + str(self.tree2str(root.left)) + ')(' + str(self.tree2str(root.right)) + ')'