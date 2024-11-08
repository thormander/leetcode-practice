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

            if slow == fast:
                return True
        
        return False


'''
to check if we have a cycle
 - slow and fast pointer strat
 - slow increments once
 - fast incremets twice
eventually they will hit each other so we know there is a cycle
'''
        
