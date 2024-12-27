class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        
        visited_cells = set()

        def dfs(row,column,index_word):
            # base cases
            if index_word == len(word):
                return True
            
            # bounds
            if column < 0 or row < 0 or column >= columns or row >= rows:
                return False
            if word[index_word] != board[row][column]:
                return False
            if (row,column) in visited_cells:
                return False

            visited_cells.add((row,column))
            # recursion/traversal (go up,down,left,or right)
            result = (dfs(row + 1,column,index_word + 1) or
                      dfs(row - 1,column,index_word + 1) or
                      dfs(row,column + 1,index_word + 1) or
                      dfs(row,column - 1,index_word + 1) 
                     )

            visited_cells.remove((row,column))
            return result
        
        for row in range(rows):
            for col in range(columns):
                result = dfs(row,col,0)
                if result == True:
                    return True
        
        return False

'''
get the dimensions of the matrix
rows = length of the board
columns = length of some row

visited = a set to store the cells we visisted

def dfs (column, row, index):
    if index is same as word length, we know it is there so
        reutrn true
    
    if we are out of bounds
        return false
    if the letter is not same as in index
        return false
    if the cell is already visited
        return false
    
    add current cell we are on
    go either up,down,left, or right
        so 4 calls on the DFS function here

    remove the cell we added previously as we are moving on

we run this dfs on each cell in the matrix
    if we get a true just return

return false automatically if we get through the loop w/o returning true
'''
