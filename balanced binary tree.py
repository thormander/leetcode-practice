# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # dfs
        def dfs(node):

            # handle base case
            if node == None:
                return [True,0] 
            
            digleft = dfs(node.left)
            digright = dfs(node.right)

            # is it balanced?
            balanced = None
            
            if (digleft[0] == True and digright[0] == True) and (abs(digleft[1] - digright[1]) <= 1):
                balanced = True
            else:
                balanced = False
            
            return [balanced,max(digleft[1],digright[1]) + 1]
        
        result = dfs(root)

        return result[0]


'''
start from the bottom --> dfs

want to return not only whether its balance, but also height as we go back up
 - need to use height to determine if balanced for higher level nodes

recusive dfs:
    return [True or False, height]

dfs(root)

return the boolean value from the list
'''
        
