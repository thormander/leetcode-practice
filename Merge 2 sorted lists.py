# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        dummy = ListNode()
        d = dummy

        while l1 and l2:
            if l1.val < l2.val:
                d.next = l1
                l1 = l1.next
                d = d.next
            else:
                d.next = l2
                l2 = l2.next
                d = d.next  

        # handle case of one list longer than the other
        if l1:
            d.next = l1
        elif l2:
            d.next = l2

        return dummy.next            
            



'''
2 lists --> 1 list but sorted (2 lists are already sorted)

traverse both lists at the same time
 - compare the values between the pointers, whatever is less we add to the merged list
 - need a temp or dummy node to start our initial merged list.
'''
