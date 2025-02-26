# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        result = [] # store values of nodes we can see

        if root:
            queue.append(root)

        while queue:

            # check right most value in the layer while it is complete
            result.append(queue[-1].val)
            
            # processing the layer
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
        
        return result






'''
only output nodes that can be seen from right

BFS
 - build up the layer, once the layer is done --> get the right most value from the queue

result = []
queue. = [1]
'''
