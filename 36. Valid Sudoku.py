class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                # if empty or . skip
                if board[r][c] == ".":
                    continue
                
                # check if in hashsets
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in box[(r//3,c//3)]:
                    return False

                # add to hashsets/maps
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                box[(r//3,c//3)].add(board[r][c])

        
        return True



'''
rule 1
    - hashset check for duplicate, iterate through each row

rule 2
    - hashset check for duplicate, iterate through each col

rule 3
    - 9 sub-boxes
    - start with 012 index then to get to next we just add 3


between the 3 rules:
    hashmap ==> key: row/col/subbox | value: set()

    for the sub boxes, use // when dividing to figure out which box we are in


'''
