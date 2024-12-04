# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.result = 0
        
        def dfs(node,maxNum):
            # base case
            if not node:
                return 0
            
            # check if our current node is a good node
            if node.val >= maxNum:
                self.result += 1
            
            # dfs
            dfs(node.left,max(maxNum,node.val))
            dfs(node.right,max(maxNum,node.val))
        
        dfs(root,root.val)

        return self.result



'''
DFS
running result

make another function to pass the max number down to children nodes when we recurse:
    - base case is if node is none, just return 0
    - check if current node value > value passed down from recursion
        - if it is result += 1
    - dfs down left and right
'''
