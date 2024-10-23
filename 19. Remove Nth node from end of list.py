# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        
        # postiion our right pointer
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # after this, our pointers are in place, we shift both until right is null
        while right:
            left = left.next
            right = right.next
        
        # delete our nth node
        left.next = left.next.next

        return dummy.next # exclude dummy node



'''
reverse the list, but we would need to do it again
- not ideal

d [1,2,3,4,5]
        L    R 

need to start L before the list (or a dummy node)
 - keep r in original spot, but left should start at the dummy
'''
