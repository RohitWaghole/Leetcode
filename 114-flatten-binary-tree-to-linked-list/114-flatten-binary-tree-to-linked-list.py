# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T.C. -> O(N)
# S.C. -> O(N)

# class Solution:
#     def __init__(self):
#         self.prev = None
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         if root==None:
#             return 
#         self.flatten(root.right)
#         self.flatten(root.left)
        
#         root.right = self.prev
#         root.left = None
#         self.prev = root

#######################################################################################

# T.C. -> O(N)
# S.C. -> O(N)

# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         if not root:
#             return
#         stack = [root]
#         while stack:
#             curr = stack.pop()
#             if curr.right:
#                 stack.append(curr.right)
#             if curr.left:
#                 stack.append(curr.left)
#             if stack:
#                 curr.right = stack[-1]
#             curr.left = None

#######################################################################################

# T.C. -> O(N)
# S.C. -> O(1)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        curr = root
        while curr:
            
            if curr.left:
                prev = curr.left
            
                while prev.right:
                    prev = prev.right

                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
        
            curr = curr.right
        
        
        