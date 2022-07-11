# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ds = []
        self.reversePreorder(root,0,ds)
        return ds[-1]
        
    def reversePreorder(self,root,level,ds):
        if root:
            
            if level==len(ds):
                ds.append(root.val)
            self.reversePreorder(root.left,level+1,ds)
            self.reversePreorder(root.right,level+1,ds)