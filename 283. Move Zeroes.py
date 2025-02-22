class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point = 0

        # first pass
        for i,v in enumerate(nums):
            if v != 0:
                nums[point] = v
                point += 1
        
        # second pass
        for i in range(point,len(nums)):
            nums[i] = 0



'''
keep a pointer at begging

if we run into case of non-zero, move that to pointer and increment it

second pass we take any index pass the pointer and set to 0
'''
