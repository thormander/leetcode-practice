class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i] # right neighbor
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= postfix
            postfix *= nums[i] # left neighbor
        
        return answer
        
        
        '''
        declare array of length nums; fill with ones

        create a prefix that will increment.          (n)
            left --> right of answer array
            put prefix in answer array
            multiply prefix to right element -- update prefix

        create a postfix that will decrement         (n)
            right --> left of answer array
            multiply postfix to answer array element
            multpliy itself to left element -- update postfix



        O(n)
        '''
