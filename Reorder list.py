# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. find midpoint of our linked list
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. reverse our second half (slow.next is start of our second half)
        prev = None
        current = slow.next
        slow.next = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        # 3. merge back together
        right = prev
        left = head
        while right:
            tempL = left.next
            tempR = right.next

            left.next = right
            right.next = tempL
            left = tempL
            right = tempR




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                


'''
we cant use extra memory

one pointer at start and end
 - simply shift the end and fix the pointers...

1. Find midpoint of our linked list (fast and slow pointer method)
2. need to reverse the last half so we can go in reverse
3. mere the two together makign sure we point them properley

- edge case: make sure end of the first half points to null
'''
        
