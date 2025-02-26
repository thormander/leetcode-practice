# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0 # amount of good nodes

        def DFS(node,max_seen):
            # base case
            if not node:
                return 0
            
            # check if good node
            if node.val >= max_seen:
                self.result += 1
            
            # recursion case
            DFS(node.left,max(max_seen,node.val))
            DFS(node.right,max(max_seen,node.val))
        
        DFS(root,root.val)

        return self.result





'''
DFS
result = keeps track of good nodes we run into

need to worry about any previous nodes that are bigger
    - keep a running max on our previous nodes

DFS function(node, previous max value we have ran into):
    base case
    check if current node is actually greater than max
        if it is we found a good node
    recursion case
'''
        
