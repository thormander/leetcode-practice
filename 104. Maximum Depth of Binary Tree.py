# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        layer = 0

        queue = deque()

        if root:
            queue.append(root)

        while queue:
            # we want to go layer by layer
            for i in range(len(queue)):
                cur_node = queue.popleft()

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
            layer += 1
            

        
        return layer



'''
DFS --> dig as far down as possible nad just keep a runnig max

*** BFS --> go layer by layer and return our last layey ***

keep track of layer we are on

do the bfs until we stop and then return the layer we are on

'''
        
