# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        queue = deque()
        queue.append(root)

        while queue:
            rightmost = None

            for i in range(len(queue)):
                popped = queue.popleft()

                if popped:
                    rightmost = popped.val
                    queue.append(popped.left)
                    queue.append(popped.right)
            
            if rightmost != None:    
                result.append(rightmost)
                    
        return result

        
        '''
        BFS; add right most node for the level 
        '''
