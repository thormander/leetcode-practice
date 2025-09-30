class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            midpoint = (left+right) // 2

            if nums[midpoint] == target:
                return midpoint
            
            if nums[midpoint] > target:
                right = midpoint - 1
            else:
                left = midpoint + 1
        
        return left
        

'''
log(n) --> binary search

standard binary search

[1,3,5,6] target = 2
 |
'''
