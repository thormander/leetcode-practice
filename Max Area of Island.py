class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set() # holds (r,c) pairs

        # dfs
        def DFS(r,c):
            # base case
            if (r < 0 or r == rows or c < 0 or c == cols) or (grid[r][c] == 0) or ((r,c) in visited):
                return 0

            visited.add((r,c))

            return (1 + DFS(r+1,c) +
                        DFS(r-1,c) +
                        DFS(r,c+1) +
                        DFS(r,c-1))
            

        # iterate over grid; call DFS when we we encounter '1'
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result = max(result,DFS(r,c))
        
        return result
        
        '''
        area = amount of 1s basically

        DFS; calc area and compare with overall result and replace if more
        use hashset to see visited nodes
        '''
