class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            # base case
            if nums[mid] == target:
                return mid
            # case when mid is less than target
            elif nums[mid] < target:
                left = mid + 1
            # case when mid is greater than target
            else:
                right = mid - 1

        return -1




'''
binary search

if some target doesnt exist jsut return -1, otherwise return the index it is at.
'''
