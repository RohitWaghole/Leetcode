# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        start = start_node = ListNode(0)
        after = after_node = ListNode(0)
        
        while head:
            
            if head.val < x:
                
                start.next = head
                start = start.next
                
            else:
                
                after.next = head
                after = after.next
                
            head = head.next
            
        after.next = None
        
        start.next = after_node.next
        
        return start_node.next