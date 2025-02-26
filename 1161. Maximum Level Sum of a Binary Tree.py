# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque()

        if root:
            queue.append(root)

        sum_layers = [] # store sums of each layer (0-indexed)
        
        while queue:

            # get the sum
            queue_vals = []
            # get node values
            for node in queue:
                queue_vals.append(node.val)
            
            sum_layers.append(sum(queue_vals))
            
                
            # process nodes
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        
        return sum_layers.index(max(sum_layers))+1


'''
bfs
 - layer by layer

keep a running max on val
'''
