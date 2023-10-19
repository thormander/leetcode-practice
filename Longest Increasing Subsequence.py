class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                # [0,1,0,3,2,3]
                #        ^ ->
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i],1+cache[j])
        
        return max(cache)
        '''
        DP; go in reverse
        '''
