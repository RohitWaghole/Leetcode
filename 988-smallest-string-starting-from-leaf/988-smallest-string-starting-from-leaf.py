# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        self.res = '~'
        def f(root,ds):
            
            if not root:
                return False
            
            ds.append(chr(root.val+97))
            left = f(root.left, ds)
            right = f(root.right, ds)
            
            if not (left or right):
                self.res = min(self.res,''.join(ds[::-1]))
            ds.pop()
            return True
        
        f(root,[])
        return self.res