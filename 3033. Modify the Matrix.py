class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        col = len(matrix[0])
        rows = len(matrix)

        max_col_num = []

        # first pass
        for c in range(col):
            column_max = -1
            
            for r in range(rows):
                cur_num = matrix[r][c]
                column_max = max(column_max,cur_num)

            max_col_num.append(column_max)
        
        # second pass
        for c in range(col):
            for r in range(rows):
                cur_num = matrix[r][c]
                if cur_num == -1:
                    matrix[r][c] = max_col_num[c]

        return matrix

'''
given some matrix, replace any -1's with max num in the column

2 passes over the matrix
    - 1. know what is max of each col
    - 2. replace -1's with corresponding max

save a bit on memory by using input matrix instead of making a copy

0 1 2
'''
