# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head == None or head.next == None:
            return head # if we get empty list or list size 1
        
        odd = head
        even = head.next
        even_head = head.next
        
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        # set odd pointer at end to point at even
        odd.next = even_head

        return head


            

'''
[1,2,3,4,5] 
         o 
            e

get all odd to front, even after
order keep same as is

they use node index NOT VALUE (1-indexed)

base case check make sure its at least 2
'''
