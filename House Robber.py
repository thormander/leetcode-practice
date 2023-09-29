class Solution:
    def rob(self, nums: List[int]) -> int:
        
        evenHouses = 0
        oddHouses = 0

        for index,house in enumerate(nums):
            if index % 2 == 0: # case of even (should handle 0 properly as it is first)
                evenHouses = max(evenHouses + house, oddHouses)
            else: # case of odd
                oddHouses = max(oddHouses + house, evenHouses)
        
        return max(evenHouses,oddHouses)



        '''
        run a even,odd variable.
        take their values, but we want to take max b/t either the next even element or odd
        '''
