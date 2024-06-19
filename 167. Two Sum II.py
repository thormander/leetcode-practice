class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            # when we find answere
            if (numbers[left] + numbers[right] == target):
                return [left+1,right+1]
            
            # do our check
            if (numbers[left] + numbers[right]) < target:
                left += 1
            else:
                right -= 1

'''
"increasing" in order

use 2 pointers, one at start and one at end

check if value is our target

if it isn't:
    is it greater?
        then we want to decrement our right

    is it less?
        increase our left pointer

'''
