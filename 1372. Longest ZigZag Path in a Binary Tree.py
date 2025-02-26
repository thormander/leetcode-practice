# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.result = 0 # longest zig zag

        def DFS(node,is_left,cur_path):
            # base case
            if not node:
                return

            # check if we are bigger than result
            self.result = max(self.result,cur_path)
            
            # recursive case
            if is_left:
                DFS(node.right,False,cur_path+1) # case of going right
                DFS(node.left,True,1) # reset since left --> left
            else:
                DFS(node.right,False,1) # reset since right --> right
                DFS(node.left,True,cur_path+1) # case of goign left
            
        DFS(root,False,0)
        return self.result


'''
only increment the current path 
if its alternating only.

if it goes same side, ie right, right then just reset back to one

DFS (node, what direction, path_length)

also need a running max

'''
