class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0 # time
        freshOJ = 0 # amount of fresh oranges
         
        rows = len(grid)
        cols = len(grid[0])

        queue = deque() # rotten oranges

        # info gathering on oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshOJ += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
                else:
                    continue
        


        # BFS
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        while queue and freshOJ > 0:

            # remove all rotten as we are processing all on same layer
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c

                    if (row<0 or col<0 or row==rows or col==cols) or grid[row][col] != 1:
                        continue
                    else:
                        # fresh orange and inbound (we can make it rotten)
                        grid[row][col] = 2
                        queue.append((row,col))
                        freshOJ -= 1
            result += 1
        
        if freshOJ != 0:
            return -1
        else:
            return result
                
        '''
        Has to be BFS; each layer can be considered a minute

        inital processing BEFORE BFS!!!
            - find amount fresh and append any rotten to our queue

        queue is inital rotten oranges 

        If there is fresh oranges left, return -1 
        '''
