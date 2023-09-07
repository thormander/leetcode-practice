# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

        '''
        faster

        use slow/fast pointer

        set both to head, then just increment one 2x as much

        while loop through until one of the pointers hit null:
            if fast == slow:
                theres a cycle
                *Make sure to check after incrementing !!!*

        '''
