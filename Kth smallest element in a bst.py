# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None
        
        def DFS(node):
            # base case
            if not node:
                return 
            
            # dig far left
            DFS(node.left)

            nonlocal count
            count += 1
            
            if count == k:
                nonlocal result
                result = node.val
                return
                
            
            DFS(node.right)
        
        DFS(root)
        return result


        '''
        DFS down as far left as possible; count up k times and retrun the nodes value
        '''
        
