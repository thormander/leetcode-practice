class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(0)
        dummyNode.next = head
        pointer1 = dummyNode
        pointer2 = head
        for i in range(n):
            pointer2 = pointer2.next

        # get pointer1 to node before the one we need to remove
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        pointer1.next = pointer1.next.next
        
        return dummyNode.next




        '''
        pointer1, pointer2:

            dummy node and intiilize pointer 1 to it
            keep pointer 2 original poistion (ie. head.next * n)
        
        loop until pointer2 is null:
            if pointer2.val = None:
                set pointer1 to pointer.next.next

            .next both pointers

        '''
