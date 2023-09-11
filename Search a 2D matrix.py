class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            left = 0
            right = len(row) - 1

            # do binary search on the row
            while left <= right:
                middle = (right + left) // 2 #make sure to recalc middle
                if target > row[middle]:
                    left = middle + 1
                elif target < row[middle]:
                    right = middle - 1
                else:
                    return True
        return False


        '''
        binary search

        for each row in matrix:
            perform binary sarch
            if target found:
                return True
            else:
                if nothing found, continue
        
        return False

        '''
