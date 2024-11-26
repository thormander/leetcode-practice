# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        current_node = root

        while True:

            # case 1
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            # case 2
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            else:
                return current_node





'''

case where both are greater
    - search right side

case where both are less
    - search left side

LCA = any time p < current node < q
    - basically the split

anytime they both arent greater or less, we can jsut return the node we are on
    - this still holds true for case where p or q is on our LCA

we are guarenteed a result because p and q exist in the given tree
'''
