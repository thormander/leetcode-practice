# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = deque()
        queue.append(root)

        result = []

        while queue:
            layer_size = len(queue)
            for i in range(layer_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if i == layer_size - 1:
                    result.append(node.val)
            

            
        
        return result

        


        

'''
essentially, taking right most value for each layer

BFS --> since we need to go layer by layer
    - first get length of queue then iterate through it --> we know when we are in another layer (or at end of current)
    - when we reach end of our layer (or after we are done processing it), grab it and add to result list
'''
