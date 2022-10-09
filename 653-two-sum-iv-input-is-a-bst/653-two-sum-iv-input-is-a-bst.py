# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(root):
            if root:
                yield from inorder(root.left)
                yield root.val
                yield from inorder(root.right)
                
        def inorderReverse(root):
            if root:
                yield from inorderReverse(root.right)
                yield root.val
                yield from inorderReverse(root.left)
                
        a = inorder(root)
        b = inorderReverse(root)
        
        left, right = next(a), next(b)
        
        while left<right:
            if left + right == k:
                return True
            
            if left + right > k:
                right = next(b)
            else:
                left = next(a)
                
        return False
                
        
#         def preorder(root, seen):
#             if root==None: return False
#             c = k - root.val
#             if c in seen: return True
#             seen.add(root.val)
#             return preorder(root.left, seen) or preorder(root.right, seen)
        
#         return preorder(root,set())