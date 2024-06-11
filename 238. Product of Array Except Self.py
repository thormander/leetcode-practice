class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums) # [1,1,1,1]

        pre = 1
        post = 1

        # first pass
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        
        # second pass -- reverse
        for i in range(len(nums)-1,-1,-1):
            output[i] *= post
            post *= nums[i]
        
        return output


'''
[1,2,3,4]

1 [1,1,1,1]
pre 
1st iteration
1 [1,1,1,1] 

pre * current index or 0 and update that value

2nd iteration will give us a 1 again

3rd 
1 [1,1,2,1]
pre = 2

4th
1 [1,1,2,6]
pre = 2 * 3 = 6 

essential do the same in reverse order
[1,1,2,6] 1
         post
'''


