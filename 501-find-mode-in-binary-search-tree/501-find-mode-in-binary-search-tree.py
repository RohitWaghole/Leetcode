# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.d = {}
        
        def traverse(root):
            
            if root:
                traverse(root.left)
                self.d[root.val] = self.d.get(root.val, 0)+1
                traverse(root.right)
                
        traverse(root)
        res = []
        mx = max(self.d.values())
        for key,val in self.d.items():
            if val==mx: res.append(key)
        return res