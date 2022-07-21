# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd = ListNode(0)
        oddDummy = odd
        even = ListNode(0)
        evenDummy = even
        
        i = 1
        while head:
            if i%2==0:
                evenDummy.next = head
                evenDummy = evenDummy.next
            else:
                oddDummy.next = head
                oddDummy = oddDummy.next
            head = head.next
            i+=1
        evenDummy.next = None
        oddDummy.next = even.next
        return odd.next