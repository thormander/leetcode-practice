# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def DFS(root):
            # base case
            if not root:
                return [True,0]

            left = DFS(root.left)
            right = DFS(root.right)

            
            # say it is true when height not greater than 1, and subtress are also valid
            balanced = False  
            if abs(left[1] - right[1]) < 2 and left[0] and right[0]:
                balanced = True

            return [balanced, 1 + max(left[1],right[1])]
            
            
        return DFS(root)[0]

        '''
        use DFS, start at bottom
        determine whether it is balanced pass [bool,height]
        '''
        
