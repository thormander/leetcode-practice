class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # rows in a hashset
        seen_rows = {}
        for row in grid:
            if tuple(row) not in seen_rows:
                seen_rows[tuple(row)] = 1
            else:
                seen_rows[tuple(row)] += 1
        
        result = 0

        for col_i in range(len(grid)):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col_i])
            
            # if we can make a pair
            if tuple(column) in seen_rows:
                result += seen_rows[tuple(column)]
        
        return result



'''
hashset rows = store rows we came across
hashset cols = store cols we came across --> dont think we nee this

fill rows first

one pass on cols and check if they match a row in hashset
'''
