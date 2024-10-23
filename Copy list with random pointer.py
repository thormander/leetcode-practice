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

        hashmap = {None : None} # old node : new node

        #1. first pass, just make copies and map old to clones
        p = head
        while p:
            clone = Node(p.val)
            hashmap[p] = clone
            p = p.next

        #2. second pass, fix pointers
        p = head
        while p:
            clone = hashmap[p]
            clone.next = hashmap[p.next]
            clone.random = hashmap[p.random]
            p = p.next
        
        return hashmap[head]
        
'''
deep copy
- node can have 2 pointers, one oints to next and another random

1. pass through linked list, and make node copies ONLY
 - no linking, but we can use a map to link our old node to the copy
 - need some way to look up what the old node points at

2. second pass do the links for the copies based on old nodes; 
 - reference our map to help us with this
'''
