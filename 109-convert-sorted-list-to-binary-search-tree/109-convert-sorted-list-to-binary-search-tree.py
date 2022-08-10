# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
#         l = []
#         while head:
#             l.append(head.val)
#             head = head.next
        
#         def f(start,end):
#             if start>end:
#                 return None
#             mid = (start+end)//2
#             root = TreeNode(l[mid])
#             root.left = f(start,mid-1)
#             root.right = f(mid+1,end)
#             return root
#         return f(0,len(l)-1)


####################################################################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        slow,fast = head,head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        root = TreeNode(mid.val)
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
    
    
    