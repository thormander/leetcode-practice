# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def DFS(root):
            nonlocal result
            if not root:
                return -1

            left = DFS(root.left)
            right = DFS(root.right)

            result = max(result, 2 + left + right)

            return 1 + max(right,left)
        
        DFS(root)
        
        return result
            
        '''
        max diameter = furthest down on the right and left of the tree
        edges = amount nodes - 1
        '''
