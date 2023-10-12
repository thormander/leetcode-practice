class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        path = set()

        def DFS(r, c, i):
            # base cases
            if len(word) == i:
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r,c) in path: # bounds
                return False
            
            path.add((r,c))
            # search around current position
            result = DFS(r+1,c,i+1) or DFS(r-1,c,i+1) or DFS(r,c+1,i+1) or DFS(r,c-1,i+1)
            path.remove((r,c))

            return result

        for r in range(rows):
            for c in range(cols):
                if DFS(r,c,0):
                    return True
        
        return False
