class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else: # equality
                tail.next = list1
                list1 = list1.next
        
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


        '''
        need dummy node for output list

        compare values between l1 and l2:
            insert l1 if less
            insert l2 if less

        make sure to add remaing nodes if l1 or l2 is longer

        return dummy.next
        '''
