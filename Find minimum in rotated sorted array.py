class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]

        left = 0
        right = len(nums) - 1


        
        #binary search
        while left <= right:
            # case where we have a sorted portion
            if nums[left] <= nums[right]:
                result = min(result,nums[left])

            mid = (left + right) // 2

            result = min(result,nums[mid])

            # figure out what section mid is part of
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return result


'''
logn -> binary search

l    m    r

figure out which section our midpoint is at
left sectio and right

anytime nums[mid] >= nums[left], we know midpoint is in left section --> want to search to the right of it

inital check
if left <= right: basically sorted array and re can return the left
else we go left
'''    
