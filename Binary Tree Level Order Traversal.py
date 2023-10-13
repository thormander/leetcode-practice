# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []

        queue = deque()
        queue.append(root)

        while queue:
            levelNodes = []

            for i in range(len(queue)):
                nodePopped = queue.popleft()
                if nodePopped:
                    levelNodes.append(nodePopped.val)
                    queue.append(nodePopped.left)
                    queue.append(nodePopped.right)
            if levelNodes:
                result.append(levelNodes)

        return result
        '''
        BFS; use deque
        '''
        
