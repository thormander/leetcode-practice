# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # handle base case
        if root == None:
            return None
        
        queue = deque([root]) # first start with root

        # do bfs
        while queue:
            cur_node = queue.popleft()

            # reverse it
            temp = cur_node.right
            cur_node.right = cur_node.left
            cur_node.left = temp

            # if it has a child
            if cur_node.right:
                queue.append(cur_node.right)
            
            if cur_node.left:
                queue.append(cur_node.left)
        
        return root


            



'''
start from root
just swap left with right

either do BFS or DFS --> BFS

deque = first add root to

'''
