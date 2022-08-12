# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.s = 0
        
        def f(root,s):
            
            if not root:
                return False
            
            s.append(root.val)
            left = f(root.left, s)
            right = f(root.right, s)
            
            if not (left or right):
                self.s += int(''.join(str(i) for i in s))
            
            s.pop()
            return True
        
        f(root, [])
        
        return self.s