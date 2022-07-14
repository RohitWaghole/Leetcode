# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_hashmap = {}
        for i in range(len(inorder)):
            inorder_hashmap[inorder[i]]=i
        
        return self.build_Tree(preorder, 0, len(preorder)-1, inorder,0,len(inorder)-1, inorder_hashmap)
    
    def build_Tree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inorder_hashmap):
        
        if preStart>preEnd or inStart>inEnd:
            return None
        
        root = TreeNode(preorder[preStart])
        inRoot = inorder_hashmap[root.val]
        numsLeft = inRoot - inStart
        
        root.left = self.build_Tree(preorder,preStart+1,preStart+numsLeft, inorder,inStart,inRoot-1, inorder_hashmap)
        
        root.right = self.build_Tree(preorder,preStart+numsLeft+1,preEnd, inorder,inRoot+1,inEnd, inorder_hashmap)
        
        return root