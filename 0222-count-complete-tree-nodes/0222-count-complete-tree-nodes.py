# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def inorder(root):
            if root:
                inorder(root.left)
                if root.val!='a':
                    self.res += 1
                    root.val = 'a'
                inorder(root.right)
        inorder(root)
        return self.res