# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def DFS(node,left_bound,right_bound):

            # base cases
            if not node:
                return True
            
            if not (left_bound < node.val and node.val < right_bound):
                # when it does not hold
                return False
            
            # recursion
            left = DFS(node.left,left_bound,node.val)
            right = DFS(node.right,node.val,right_bound)

            if left == right == True:
                return True
            else:
                return False
        
        return DFS(root,float('-inf'),float('inf'))

        

            

'''
DFS

start top --> bottom

as we go down, we check is current node within the bounds

root = [2,1,3]

say we start at root: - infinity < 2 < infinity --> return True, so we move on

we go left --> - infinity (left bound same) < 1 < 2 -->  true

same for right jsut cahnge the left bound and keep right bound same

--------------

base cases:
    null node , return True
    value checking

dfs to left side
dfs to right

'''
