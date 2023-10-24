class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # base case
        if not grid:
            return 0
        
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        # BFS
        def BFS(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                row,col = queue.popleft()
                # all adjacent cells
                directions = [[1,0],[0,1],[-1,0],[0,-1]]

                # check around current cell
                for n_row, n_col in directions:
                    if (row + n_row) in range(rows) and (col + n_col) in range(cols) and grid[row+n_row][col+n_col] == "1" and (row+n_row,col+n_col) not in visited:
                        
                        queue.append((row+n_row,col+n_col))
                        visited.add((row+n_row,col+n_col))

        # iterate through grid
        for r in range(rows):
            for c in range(cols):

                # conditions for 'new' island
                if grid[r][c] == "1" and (r,c) not in visited:
                    BFS(r,c)
                    result += 1

        return result
        
        '''
        BFS; increment amount of islands whenever we run into a 1 that has not been visted and is not in queue
            - have a visited set
        '''
