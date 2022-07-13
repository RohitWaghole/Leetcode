# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        if not root:
            return result
        
        queue = deque([root])
        
        while queue:
            
            l = len(queue)
            level = []
            for i in range(l):
                
                node = queue.popleft()
                
                if node.left!=None: queue.append(node.left)
                if node.right!=None: queue.append(node.right)
                    
                level.append(node.val)
            
            result.append(level)
            
        return result