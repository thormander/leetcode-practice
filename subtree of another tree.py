# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(a,b):
            if not a and not b:
                return True # base case
            elif a and b and a.val == b.val:
                return sameTree(a.right, b.right) and sameTree(a.left, b.left)
            else:
                return False

        # base case
        if not subRoot:
            return True
        elif not root:
            return False
        
        if sameTree(root,subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


