# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.result = []
        def f(root):
            if root:
                self.result.append(root.val)
                f(root.left)
                f(root.right)
        f(root)
        return self.result