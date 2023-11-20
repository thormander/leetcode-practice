class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)

        pre = 1
        post = 1

        # first run through
        for i, v in enumerate(nums):
            result[i] = pre
            pre = pre * v

        # second run through (backwards)
        for i in range(len(nums)-1,-1,-1):
            result[i] = result[i] * post
            post = post * nums[i]

        return result


        '''
        need a pre and post

        first run through, need to calc result going left -> right
        second run throught, calc result going right -> left

        work within one list result
        '''
