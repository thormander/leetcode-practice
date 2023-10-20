class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # base case
        if sum(nums) % 2 != 0:
            return False

        hashset = set()
        hashset.add(0)

        for i in range(len(nums)-1,-1,-1):
            tempSet = hashset.copy()
            for val in hashset:
                tempSet.add(nums[i]+val)
            hashset = tempSet
        
        if sum(nums) // 2 in hashset:
            return True
        else:
            return False




        '''
        take sum, if not divisible by 2, then we can return false

        hashset; go in reverse order, 

        [1,5,11,5]  half = sum/2

        cache = [0] -> [0,5] -> [0,5,11,16]
            since 11 = half we can go ahead and return true
        if nothing == half, just return false
        '''
