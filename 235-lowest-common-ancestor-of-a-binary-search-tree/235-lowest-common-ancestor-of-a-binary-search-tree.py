# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         def f(root,target,ds):
#             if not root:
#                 return False
#             ds.append(root.val)
#             if root==target:
#                 return True
#             left = f(root.left,target,ds)
#             right = f(root.right,target,ds)
            
#             if left or right:
#                 return True
#             ds.pop()
#             return False
        
#         l1,l2 = [],[]
#         f(root,p,l1)
#         f(root,q,l2)
        
#         i,j = 0,0
#         while i<len(l1) and j<len(l2) and l1[i]==l2[j]:
#             i+=1
#             j+=1
#         return TreeNode(l1[i-1])

##############################################################################################################

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         if root==None or root==p or root==q:
#             return root
        
#         left = self.lowestCommonAncestor(root.left,p,q)
#         right = self.lowestCommonAncestor(root.right,p,q)
#         if left==None:
#             return right
#         if right==None:
#             return left
#         return root

#############################################################################################################

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         while root:
#             if p.val < root.val > q.val:
#                 root = root.left
#             elif p.val > root.val < q.val:
#                 root = root.right
#             else:
#                 return root



















#############################################################################################################

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def f(root, target, ds):
            
            if root:
                
                ds.append(root.val)
                if root==target:
                    return True
                
                left = f(root.left, target, ds)
                right = f(root.right, target, ds)
                
                if left or right:
                    return True
                ds.pop()
                
            return False
        
        l1,l2 = [],[]
        f(root, p, l1)
        f(root, q, l2)
        
        i,j=0,0
        while i<len(l1) and j<len(l2) and l1[i]==l2[j]:
            i+=1
            j+=1
        return TreeNode(l1[i-1])






















