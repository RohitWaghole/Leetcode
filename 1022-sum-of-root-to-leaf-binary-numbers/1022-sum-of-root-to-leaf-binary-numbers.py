# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(ans,s,root):
            if root.left:
                dfs(ans,s+str(root.val),root.left)
            if root.right:
                dfs(ans,s+str(root.val),root.right)
                
            if not (root.left or root.right):
                s+=str(root.val)
                ans.append(s[:])
        
        
        ans=[]
        d=0
        dfs(ans,'',root)
        return sum(int(i,2) for i in ans)
            