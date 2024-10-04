# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        placeholder = ListNode()
        p = placeholder

        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            
            p = p.next
        
        # case where one is longer than the other (we jsut add it at the end)
        if list1:
            p.next = list1
        else:
            p.next = list2

        return placeholder.next



'''
start a new list node, for our pupose use a placeholder or dummy

____ -> 1 -> 1 -> 2 -> 3
'''
