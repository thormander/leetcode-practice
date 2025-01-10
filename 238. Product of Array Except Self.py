class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1

        result = [1] * len(nums)

        # 1st step (l --> r)
        for i in range(len(nums)):
            result[i] = pre # set
            pre *= nums[i] # update

        # 2nd step (r --> l)
        for i in range(len(nums)-1,-1,-1):
            result[i] *= post # set
            post *= nums[i] # update
        
        return result

'''
[1,2,3,4]

pre and post

1st step

pre start at 1(left to right) --> at the index that is the result of multiplying nums to left of that number
[1,1,2,6]

insert pre to i on the result list, then update it by * the current num we are on

2nd step (go in reverse)
post start 1
[24,12,8,6] 

SET then UPDATE

'''
