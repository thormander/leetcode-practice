class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # create our hashamps wiith value as a hashset
        hashRow = defaultdict(set)
        hashColumn = defaultdict(set)
        hashBox = defaultdict(set)

        for row in range(9):
            for col in range(9):
                # base case checks
                if board[row][col] == ".":
                    continue
                if board[row][col] in hashRow[row] or board[row][col] in hashColumn[col] or board[row][col] in hashBox[(row//3,col//3)]:
                    return False
                
                # add to hashmap
                hashRow[row].add(board[row][col])
                hashColumn[col].add(board[row][col])
                hashBox[(row//3,col//3)].add(board[row][col])

        
        return True


'''
row duplicates
 - hashmap -> key: indexRow | value: hashset
column duplicates
 - same as above
each sub box:
 - whole number division --> round to get our indexing our key: index r/3 , index c/3
 - same idea as above

'''
