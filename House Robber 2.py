class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # edge case
        if len(nums) < 2:
            return nums[0]

        def helper(startIndex,endIndex):
            evenHouses = 0
            oddHouses = 0
            for i in range(startIndex,endIndex):
                if i % 2 == 0: # even
                    evenHouses = max(evenHouses + nums[i],oddHouses)
                else: # odd
                    oddHouses = max(oddHouses + nums[i],evenHouses)
            return max(evenHouses,oddHouses)           

        return max(helper(0,len(nums)-1),helper(1,len(nums)))   
        
        '''
        DP; possibly iterate only until 2nd to last?

        then when we finish getting max values from odd/even houses, we can take the max b/t odd + last     element vs even
        '''
