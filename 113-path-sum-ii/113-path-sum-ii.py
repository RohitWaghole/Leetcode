# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        
#         self.res = []
#         def f(root,target,ds,s):
            
#             if not root:
#                 return False
            
#             ds.append(root.val)
#             s += root.val
            
#             left = f(root.left,target,ds,s)
#             right = f(root.right,target,ds,s)
            
#             if not left and not right:
#                 if s==target:
#                     self.res.append(ds[:])
#             s -= ds.pop()
#             return True
#         f(root,target,[],0)
#         return self.res








class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        
        self.res = []
        
        def f(root,ds,s):
            if not root:
                return False
            
            ds.append(root.val)
            s += root.val
            left = f(root.left,ds,s)
            right = f(root.right,ds,s)
            
            if not(left or right):
                if s==target:
                    self.res.append(ds[:])
            ds.pop()
            s -= root.val
            return True
        
        f(root,[],0)
        return self.res
































