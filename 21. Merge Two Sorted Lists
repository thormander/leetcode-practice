# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        p_builder = dummy

        # 1. do up until we hit None for either
        while list1 and list2:
            if list1.val > list2.val:
                p_builder.next = list2
                p_builder = p_builder.next

                list2 = list2.next
            else:
                p_builder.next = list1
                p_builder = p_builder.next

                list1 = list1.next                

        # 2. check if one is not none, and append to end of result list
        while list1:
            p_builder.next = list1
            p_builder = p_builder.next

            list1 = list1.next   
        
        while list2:
                p_builder.next = list2
                p_builder = p_builder.next

                list2 = list2.next

        return dummy.next


'''
[1,2,4]
       |
[1,3,4,5,6,7]
             |
dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 [5,6,7]
         |
after we go through and hit a None
    - check if one of the pointers is not null yet and just append nodes until we hit none
'''
