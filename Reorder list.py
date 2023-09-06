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
        # get middle of list (slow = middle)
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tempSplit = slow.next
        slow.next = None # split list

        # reverse second half
        prev = None
        cur = tempSplit # head of second half
        while cur:
            tempSecond = cur.next
            cur.next = prev
            prev = cur
            cur = tempSecond

        # merge back together
        left = head
        right = prev
        while right:
            tempL = left.next
            tempR = right.next
            left.next = right
            right.next = tempL
            # update pointers
            left = tempL
            right = tempR

        





        '''
        find the middle of the list:
            if odd, should not affect outcome
            use a slow/fast pointer that increments up until fast encounters null and fast.next is null
        
        split the list by making middle point to null

        reverse the second half in order to go in decreasing order

        merge the 2 lists back together
        '''
