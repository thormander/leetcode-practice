# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # base case
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:pos+1],inorder[:pos])
        root.right = self.buildTree(preorder[pos+1:],inorder[pos+1:])

        return root
