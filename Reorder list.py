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

        # 1. find midpoint (slow and fast pointer)
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # after this, our slow should be at our midpoint

        # 2. reverse right half
        right = slow.next
        slow.next = None
        dummy = None
        while right:
            temp = right.next
            right.next = dummy
            dummy = right
            right = temp

        # 3. Do the rearrangeing
        left = head
        right = dummy
        while right:
            temp1 = left.next
            temp2 = right.next

            left.next = right
            right.next = temp1
            left = temp1
            right = temp2


        
'''
1. find the midpoint
 - need to point midpoint at null !
2. need to reverse it (but not the whole thing) up to the midpoint
3. Change the pointers to fit logic in the question
 - think of left and right sie start at both and come inwards
'''
        
