class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # First binary search (check rows)
        topRow = 0
        botRow = len(matrix) - 1
        
        while topRow <= botRow:
            midRow = (botRow + topRow) // 2

            if target < matrix[midRow][0]:
                botRow = midRow - 1
            elif target > matrix[midRow][-1]:
                topRow = midRow + 1
            else:
                break
        
        if not topRow <= botRow:
            return False # pointers crossed, target not in the matrix
        
        # Second binary search (searching the row)
        rowToSearch = (botRow + topRow) // 2
        left = 0
        right = len(matrix[rowToSearch]) - 1

        while left <= right:
            mid = (right + left) // 2

            if target < matrix[rowToSearch][mid]:
                right = mid - 1
            elif target > matrix[rowToSearch][mid]:
                left = mid + 1
            else:
                return True

        '''
        2 binary searchers

        first
        need to look for row the target is in

        if target not in any rows than return false

        second 
        need to look for target
        '''
        
