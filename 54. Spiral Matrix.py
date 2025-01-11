class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        # boundaries
        left = 0
        right = len(matrix[0])
        top =  0
        bottom = len(matrix)

        while left < right and top < bottom:
            # along top, l --> r
            for i in range(left,right):
                # iterating through columns
                result.append(matrix[top][i])
            top += 1

            # along right top --> bot
            for i in range(top,bottom):
                # iterating through rows now
                result.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            # along bottom r --> l
            for i in range(right-1,left-1,-1):
                # iterating through cols again
                result.append(matrix[bottom-1][i])
            bottom -= 1
            
            # along left bottom --> top
            for i in range(bottom-1,top - 1,-1):
                # iterating through rows again
                result.append(matrix[i][left])
            left += 1
        
        return result


'''
go as far right as possible,
go as far down,
go as far left,
go as far up,
... repeat from here

[1,2,3]
[4,5,6]
[7,8,9]

boundaries of the matrix (we are just starting)
left = 0
right = len(row) - 1
top = 0
bottom =  len(matrix) - 1

in python, don't need to subtract 1 as its non inclusive during range()

'''
