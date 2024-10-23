# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None # start it at None or to the left of head
        right = head

        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp
        
        return left




'''
given a list,
just need to reverse

use pointers to do this
 - need a left and right
'''
