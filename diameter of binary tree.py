# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0 

        def dfs(node):
            # base case
            if node == None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter,left+right)

            # return height
            return max(left,right) + 1
        
        dfs(root)
        
        return self.diameter




'''
DFS --> find longest path b/t two nodes

2 sub trees dig as far left and right as we can.
but, if we do it in reverse, it will make it easier as it doesnt have to go through root

diameter = 0 --> global

make an other helper function to do the dfs of the tree
    - DO NOT return diameter, we return current height!
'''
        
