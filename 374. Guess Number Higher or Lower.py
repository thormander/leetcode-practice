# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #binary search
        left = 1
        right = n
        while True:
            midpoint = (left+right) // 2

            api = guess(midpoint)

            if api == 0:
                return midpoint
            elif  api == 1:
                left = midpoint + 1
            else:
                right = midpoint - 1
        


'''
[1,2,3,4,5]
'''
