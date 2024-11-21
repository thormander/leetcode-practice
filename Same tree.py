# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # base cases
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        

        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)

        if left == False or right == False:
            return False
        else:
            return True

                

'''
recursive dfs --> go through both trees and just check if the value is the same

base cases:
 - are they same or different
 - null?

'''
