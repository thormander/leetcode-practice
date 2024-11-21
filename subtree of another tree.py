# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # helper to check if same
        def isSameTree(node,subRootNode):
            # base cases
            if node == None and subRootNode == None:
                return True
            if node == None or subRootNode == None:
                return False
            
            # at this point, we know we are not workign with empty trees
            if node.val != subRootNode.val:
                return False
            
            left = isSameTree(node.left,subRootNode.left)
            right = isSameTree(node.right,subRootNode.right)

            if left == True and right == True:
                return True
            else:
                return False
        
        # base cases for subTree recursion (similar to helper)
        if subRoot == None:
            return True
        if root == None:
            return False

        if isSameTree(root,subRoot):
            return True
        
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)

        return left or right

        

'''
need a way to check if they are same --> some helper funciton to check if same

helper is same:
    - edge cases / base case
        - are both nodes null? (if both, return true)
        - is one or the other null? (if true, return false)
        - is the value the same?

recursion
 - we can use isSubTree
 - are the 2 roots same, if not lets move on
    - if they are, we can call on helper to check if the trees are same
'''
