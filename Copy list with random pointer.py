"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hashmap = {None : None} # old node to new node

        pointer = head
        while pointer:
            newNode = Node(pointer.val)
            hashmap[pointer] = newNode

            pointer = pointer.next

        pointer = head
        while pointer:
            hashmap[pointer].next = hashmap[pointer.next]
            hashmap[pointer].random = hashmap[pointer.random]
            
            pointer = pointer.next

        return hashmap[head]


        '''
        copy --> use hash map to help

        2 passes:
        
        first:
            map original to copy
            and create the new nodes
        
        second:
            update node properites such as next and random
        '''
