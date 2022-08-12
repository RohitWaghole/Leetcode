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
            left = f(root.left, ds)
            right = f(root.right, ds)
            
            if not (left or right):
                self.result.append(ds[:])
            ds.pop()
            return True
        f(root, [])
        ans = []
        for i in self.result:
            a = '->'.join(str(c) for c in i)
            ans.append(a)
        return ans
            