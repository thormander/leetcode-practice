# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def DFS(root, maxV):
            # base case
            if not root:
                return 0
            
            # encounter good node
            if root.val >= maxV:
                nonlocal result
                result += 1

            maxV = max(maxV,root.val)

            DFS(root.right,maxV)
            DFS(root.left,maxV)
        
        DFS(root,root.val)

        return result

            

        '''
        DFS; have to continually pass the max value down
        '''
        
