# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        slow = dummy
        fast = dummy

        while fast.next and fast.next.next:
            slow = slow.next
            fast= fast.next.next
        
        # slow will be on node before middle
        slow.next = slow.next.next

        return dummy.next

'''
to remvoe, just update previous node to point at what middle is pointing at

slow pointer will land on middle

BUT we need to be one behind it, so stagger the pointers by starting on a dummy node

[1,3,4,7,1,2,6]
     s
           f
'''
