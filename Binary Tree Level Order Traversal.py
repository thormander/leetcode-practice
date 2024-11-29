# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque()
        queue.append(root)

        result = []

        while queue:
            # first grab size of queue
            levelSize = len(queue)

            layervals = []

            for i in range(levelSize):
                node = queue.popleft()

                layervals.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            # after we finish for loop, we are at end of a layer, we can take the snapshot now
            result.append(layervals)
        
        return result

    
'''
level order --> BFS

queue -> deqque

when we finish the layer we are on, take a snapshot of our quue and append it to a result list before we move on to next layer

'''
        
