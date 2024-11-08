# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy

        carryover = 0
        while l1 or l2:
            #1. get values (default 0 if null)
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val 
            if l2:
                val2 = l2.val

            #2. do the addtion
            sumNodes = val1 + val2 + carryover
            # 6 + 6 = 12 --> carryover is 1
            carryover = sumNodes // 10 # get 10's place
            valPutIn = sumNodes % 10 # get ones place

            #3. add to our result linked list
            p.next = ListNode(valPutIn)

            #4. shift pointers
            p = p.next
            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None
        
        # handle case of leftover carryover
        if carryover != 0:
            p.next = ListNode(carryover)
        
        return dummy.next
        


'''
go thorugh each list a

add it like we do elementry style with a carryover

new list for our result --> dummy node

while l1 or l2:
    1. first get the values
    2. do the addtion with carryover
    3. shift pointers

handle remaining carryover if we have

!! Handle cases where a node is null
'''
