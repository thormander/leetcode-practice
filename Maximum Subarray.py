class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += num
            result = max(currentSum,result)
        
        return result

