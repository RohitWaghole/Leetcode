# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
#         self.d = {}
        
#         def traverse(root):
            
#             if root:
#                 traverse(root.left)
#                 self.d[root.val] = self.d.get(root.val, 0)+1
#                 traverse(root.right)
                
#         traverse(root)
#         res = []
#         mx = max(self.d.values())
#         for key,val in self.d.items():
#             if val==mx: res.append(key)
#         return res

###########################################################################################################


class Solution:
    
    prev = None
    current_count = 0
    max_count = 0
    result = []
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.dfs(root)
        return self.result
    
    def dfs(self, root):
        if root:
            
            self.dfs(root.left)
            
            if root.val==self.prev:
                self.current_count += 1
            else:
                self.current_count = 1
                
            if self.current_count==self.max_count:
                self.result.append(root.val)
                
            elif self.current_count>self.max_count:
                self.result = [root.val]
                self.max_count = self.current_count
            self.prev = root.val
            
            self.dfs(root.right)

        
        
        
        
        
        
        
        
        
        
        
        
        
        