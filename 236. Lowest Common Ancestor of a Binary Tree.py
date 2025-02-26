# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def DFS(node,p,q):
            # base case
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            # recursive case
            left = DFS(node.left,p,q)
            right = DFS(node.right,p,q)

            if left and right:
                return node
            elif left and (not right):
                return left
            elif (not left) and right:
                return right
        
        return DFS(root,p,q)




'''
1. p and q are on left and right subtree
2. left side returns a num, right side returns None --> return left child
3. reverse of 2 --> return right child

DFS
- base case
- recursive case
'''
        
