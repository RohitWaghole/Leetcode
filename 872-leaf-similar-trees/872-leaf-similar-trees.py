# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def f(root,ds):
            if root:
                
                if root.left == None and root.right==None:
                    ds.append(root.val)
                f(root.left,ds)
                f(root.right,ds)
        l1 = []
        l2 = []
        f(root1, l1)
        f(root2, l2)
        return l1==l2