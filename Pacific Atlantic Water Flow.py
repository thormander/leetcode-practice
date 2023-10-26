class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = [] # hold cells that can go to both oceans

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        # DFS
        def DFS(r,c,visited,prevHeight):
            # base case
            if ((r,c) in visited) or (r<0 or c<0 or r==rows or c==cols) or (heights[r][c] < prevHeight):
                return 
            
            visited.add((r,c))

            # run on all neighbors
            DFS(r+1,c,visited,heights[r][c])
            DFS(r-1,c,visited,heights[r][c])
            DFS(r,c+1,visited,heights[r][c])
            DFS(r,c-1,visited,heights[r][c])

        # for rows touching ocean
        for c in range(cols):
            DFS(0,c,pacific,heights[0][c]) # pacific border
            DFS(rows-1,c,atlantic,heights[rows-1][c]) # atlantic border

        # for cols touching ocean
        for r in range(rows):
            DFS(r,0,pacific,heights[r][0]) # pacific border
            DFS(r,cols-1,atlantic,heights[r][cols-1]) # atlantic border
        
        # go through sets and compare
        for p in pacific:
            if p in atlantic:
                result.append(p)

        return result

        

        
        '''
        DFS; go opposite and run from edges of grid up island and combine results to see what can reach both
            oceans
        2 hashsets for pacific and atlantic
        '''
