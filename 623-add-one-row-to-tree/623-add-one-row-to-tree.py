# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        
        def f(root,depth):
            
            if root:
                
                if depth==0:
                    node = TreeNode(val)
                    node.left = root.left
                    root.left = node
                    
                    
                f(root.left,depth-1)
                f(root.right, depth-1)
                
                
                if depth==0:
                    node = TreeNode(val)
                    node.right = root.right
                    root.right = node
        f(root,depth-2)
        return root
        
                
                