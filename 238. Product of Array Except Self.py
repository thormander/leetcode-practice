class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1

        result = [1] * len(nums)

        # first pass
        for i in range(0,len(nums)):
            result[i] *= pre
            pre *= nums[i]

 
        # second pass (in reverse)
        for i in range(len(nums)-1,-1,-1):
            result[i] *= post
            post *= nums[i]

        return result


'''
pre             post
24    [1,2,3,4]   24
      [24,12,8,6]
    
first pass
    - setting that index = to what pre is , then update pre after

second
    - update result with index val * post , update post after
'''
