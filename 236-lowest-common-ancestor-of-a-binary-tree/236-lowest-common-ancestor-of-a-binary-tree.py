# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BRUTE FORCE
# T.C. -> O(N) + O(N) + O(N)
# S.C. -> O(N) + O(N)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def f(root,target,l):
            if not root:
                return False
            
            l.append(root.val)
            if root==target:
                return True
            
            left = f(root.left,target,l)
            right = f(root.right,target,l)
            
            if left or right:
                return True
            l.pop()
            return False
        
        
        l1,l2 = [],[]
        f(root,p,l1)
        f(root,q,l2)
        
        i,j = 0,0
        m,n = len(l1),len(l2)
        
        while i<m and j<n and l1[i]==l2[j]:
            i+=1
            j+=1
        
        return TreeNode(l1[i-1])
    
    
    
    
    