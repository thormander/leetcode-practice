# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        pointer = dummyNode

        carry = 0
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sumNums = num1 + num2 + carry
            carry = sumNums // 10
            sumNums = sumNums % 10
            
            newNode = ListNode(sumNums)
            pointer.next = newNode
            
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return dummyNode.next
        

        '''

        carry = 0
        loop through both lists:
            if sum < 10:
             add the nodes + carry = new node value
                 - must watch for carry value
              carry = 0
            else:
                carry = *1-9*
                new node value = 0
        
        if carry != 0: need to make sure we top off list with any carry
            new node with value = carry
            loop through till .next is null
                set it to new node

            
        '''
