class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        len_rows = len(matrix[0])

        for row in matrix:
            if row[-1] > target:
                # case where we do the binary search
                left = 0
                right = len_rows - 1

                while left <= right:
                    midpoint = (right + left) // 2
                    
                    if row[midpoint] > target:
                        # go left
                        right = midpoint - 1
                    elif row[midpoint] < target:
                        # go right
                        left = midpoint + 1
                    else:
                        return True
                
                return False
            
            elif row[-1] < target:
                continue
            else:
                return True

        return False

'''
binary search

first check top of the row
    - if top_num is > target
        stay in the row and do the search
    - elif its < target
        go to next row
    - else
        return true

return false
'''
