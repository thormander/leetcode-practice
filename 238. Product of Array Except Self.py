class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1

        result = [1] * len(nums)

        # 1st pass
        for i,v in enumerate(nums):
            result[i] *= prefix
            prefix *= v
        
        # 2nd pass
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result





'''
[1,1,2,6] 1

1 [1,1,2,6] -- 1st pass
[24,12,8,6] 12

[1,2,3,4]

prefix, postfix --> start with 1
1st pass go in order
2nd pass go in reverse

times prefix to next, then update from nums
'''  
