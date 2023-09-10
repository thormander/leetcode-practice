class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rightIndex = len(nums) - 1
        leftIndex = 0

        while leftIndex <= rightIndex:
            middle = (rightIndex + leftIndex) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                leftIndex = middle + 1
            elif nums[middle] > target:
                rightIndex = middle - 1
        
        return -1



        '''
        need to get the middle of the array

        Also: while loop while our indexs are not the same
        sorted, if value at the middle index is:
            less than:
                we need to search right
            more than:
                need to search left
            =:
                just return that index's value
        '''
