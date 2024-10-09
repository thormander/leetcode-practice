# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        placeholderX = ListNode(0,head)

        left = placeholderX
        right = head
        
        # get our right pointer in position
        while n != 0 and right:
            right = right.next
            n -= 1

        # increment both pointers by 1 now to get left pointer in position
        while right:
            left = left.next
            right = right.next
        
        # 'remove' nth node
        left.next = left.next.next
        return placeholderX.next
        

        

        

'''
2 pointers -- one pass
  [1,2,3,4,5] Null
         L     R
        
But, we actually need to be at the node before it... so we need to use a placeholder node 

 X [1,2,3,4,5] Null
        L       R
'''
