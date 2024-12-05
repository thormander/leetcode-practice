# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # root
        root = TreeNode(preorder[0])

        amount = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:amount+1],inorder[:amount])
        root.right = self.buildTree(preorder[amount+1:],inorder[amount+1:])

        return root


        

'''
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = 3
preorder = [3 | 9,20,15,7]
inorder = [9 | 3 | 15,20,7]

preorder = [X X 20,15,7]
inorder = [X X 15 | 20 | 7]



recursive
    - first create root node

'''
