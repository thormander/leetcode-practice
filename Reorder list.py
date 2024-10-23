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

        # 1. find midpoint of the list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next # 1x
            fast = fast.next.next # 2x
        
        # after this while loop, we have our midpoint at slow 
        # so start of right side is at slow.next        

        # 2. reverse the right side
        dummy = None
        curr = slow.next
        slow.next = None # handle edge case

        while curr:
            temp = curr.next
            curr.next = dummy
            dummy = curr
            curr = temp
        
        # 3. merge them together
        left = head
        right = dummy

        while right: # our right side will be smaller
            templ = left.next
            tempr = right.next

            # merge
            left.next = right
            right.next = templ

            right = tempr
            left = templ
        
        return head





'''
1. find the midpoint (fast slow pointer)
2. reverse right side of the list
    - start of right side will be the ending node; but also case where we need to point mid at None also
3. do the merge
'''
        
