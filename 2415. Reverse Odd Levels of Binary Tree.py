# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfs = deque()
        bfs.append(root)

        level = 0 # start at root

        while bfs:
            lengthCurLevel = len(bfs)

            orig = [] # store the actual node references
            copy = [] # store the node values when we reverse

            # first pass of current layer
            for i in range(lengthCurLevel):
                cur_node = bfs.popleft()
                
                if level % 2 != 0: # when odd
                    orig.append(cur_node)
                    copy.append(cur_node.val)

                # adding nodes from next layer
                if cur_node.left:
                    bfs.append(cur_node.left)
                if cur_node.right:
                    bfs.append(cur_node.right)
            
            # handle odd case (reverse)
            if level % 2 != 0:
                # 2 pointers --> top is for orig, and bot is for copy (values)
                top = 0
                bot = len(copy) - 1

                while top < len(orig):
                    # reverse the values
                    orig[top].val = copy[bot]
                    
                    # increment and decrement the pointers
                    top += 1
                    bot -= 1
            
            level += 1
        
        return root

'''
only odd level --> bfs, track what level we are on
if we are on odd level:
    - make a copy of the nodes
    - then iterate reverse through the copy and iterate normally through the original

[8,13,21,34] pretend odd (have our node references)
 ^
[8,13,21,34] iterate in reverse
          ^

bfs function:
    - deque
    - running level variable
'''
