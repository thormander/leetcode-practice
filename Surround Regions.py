class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        # DFS for capturing border "O"
        def DFS(r,c):
            # base case
            if (r<0 or c<0 or r==rows or c==cols) or board[r][c] != "O":
                return

            board[r][c] = "T"
            # run in 4 directions
            DFS(r+1,c)
            DFS(r-1,c)
            DFS(r,c+1)
            DFS(r,c-1)

        # First pass - change border "O" to something else
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    DFS(r,c)

        # Second pass - change "O" to "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # convert back to "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"        


        """
        Do not return anything, modify board in-place instead.

        DFS
        reverse-approach: find all regions that cannot be captured, capture everything else  
        2 pass:
            - first: get border regions (something non "O" so second will not intefere)
            - second: capture non-border regions O -> X
        
        Lastly, just convert border regions back to "O"
        """
        
