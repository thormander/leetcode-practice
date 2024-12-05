# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = k
        self.result = float('inf')

        def DFS(node):
            # base case
            if not node:
                return
            
            DFS(node.left)

            self.index -= 1
            if self.index == 0:
                self.result = node.val
                return

            DFS(node.right)
        
        DFS(root)
        return self.result
        

'''
DFS --> idea is dig as far left as possible, which will get us to the smallest value

var = k

DFS:

base cases --> continue, we really just need DFS for traversal

dfs to left,

decrement var by 1 (as we come back up)
check is k = 0?, if it is return that value

dfs to right side
'''
