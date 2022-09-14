# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        
        def isvalid(a):
            c = 0
            for i in a.values():
                if i%2==1:
                    c += 1
                if c>1:
                    return False
            return True
        
        def f(root,ds):
            if not root:
                return False
            
            ds[root.val] += 1
            l = f(root.left,ds)
            r = f(root.right,ds)
            
            if not (l or r):
                if isvalid(ds):
                    self.result += 1
            ds[root.val] -= 1
            return True
        
        f(root,defaultdict(int))
        return self.result