# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        def DFS(node,leaf):
            # base case
            if not node.left and not node.right:
                leaf.append(node.val)
                return

            if node.left:         
                DFS(node.left,leaf)
            if node.right:
                DFS(node.right,leaf)
            return
        
        list1 = []
        list2 = []

        DFS(root1,list1)
        DFS(root2,list2)

        return list1 == list2


            




'''
extract out leaf nodes of both tress
if they are the same, return treu

DFS
'''
