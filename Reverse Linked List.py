# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = None
        nxt = head

        while nxt:
            temp = nxt.next
            nxt.next = current
            
            # update pointers
            current = nxt
            nxt = temp
        
        return current


'''
dummy node
2 pointers, one on dummy, one on next
'''
