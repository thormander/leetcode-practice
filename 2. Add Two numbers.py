# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        numl1 = ""
        numl2 = ""

        # traverse  both lists
        pl1 = l1
        pl2 = l2

        while pl1:
            numl1 = str(pl1.val) + numl1
            pl1 = pl1.next
        
        while pl2:
            numl2 = str(pl2.val) + numl2
            pl2 = pl2.next

        sumInt = int(numl1) + int(numl2)
        
        # get to a list
        sumLists = list(str(sumInt))

        # construct our linked list
        dummy = ListNode(0)
        d = dummy
        for i in range(len(sumLists)-1,-1,-1):
            newNode = ListNode(int(sumLists[i])) # set value
            d.next = newNode
            d = newNode
        
        return dummy.next


'''
reverse order, starting from ones place

pointer at start of both, we can add as we go. 
 - handling carry overs

traverse both, get the numbers and add them for result, and then
make it a string and split it to a list
807 -> [8,0,7] --> then we want to go in reverse order and create a linked list
'''
