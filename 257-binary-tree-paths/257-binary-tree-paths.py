# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.result = []
        
        def f(root,ds):
            if root==None:
                return False
            
            ds.append(root.val)
            left = f(root.left,ds)
            right = f(root.right,ds)
            
            if left==False and right==False:
                self.result.append(ds[:])
            ds.pop()
            return True
        
        f(root,[])
        
        result = ['->'.join(str(t) for t in i) for i in self.result]
        return result