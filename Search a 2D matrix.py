class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        topRow = 0
        botRow = rows - 1

        while topRow <= botRow:
            midrow = (topRow + botRow) // 2

            leftVal = matrix[midrow][0]
            rightVal = matrix[midrow][cols-1]

            if target < leftVal:
                botRow = midrow - 1
            elif target > rightVal:
                topRow = midrow + 1
            else:
                break
                
        # second binary search
        left = 0
        right = cols - 1

        while left <= right:
            mid = (right + left) // 2

            if matrix[midrow][mid] > target:
                right = mid - 1
            elif matrix[midrow][mid] < target:
                left = mid + 1 
            else:
                return True
        
        return False
