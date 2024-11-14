# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # recursive dfs, return [is it balanced (T/F) , height]
        def dfs(node):
            if node == None:
                return [True,0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            isItBalanced = None # True or False
            if (left[0] == True and right[0] == True) and (abs(left[1] - right[1]) <= 1):
                isItBalanced = True
            else:
                 isItBalanced = False
            
            return [isItBalanced,max(left[1],right[1])+1]
        
        result = dfs(root)

        if result[0] == True:
            return True
        else:
            return False
        
