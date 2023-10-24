"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {} # old node : its clone

        def DFS(node):
            # base case
            if node in hashmap:
                return hashmap[node]
            if not node:
                return None
            
            # make clone
            clone = Node(node.val)
            hashmap[node] = clone

            # clone neighbors
            for n in node.neighbors:
                clone.neighbors.append(DFS(n))

            return clone
            
        return DFS(node)


        '''
        use a map; DFS
        '''        
