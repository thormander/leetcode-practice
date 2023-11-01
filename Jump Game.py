class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endPointer = len(nums) - 1

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= endPointer:
                endPointer = i
        
        if endPointer == 0:
            return True
        else:
            return False

        '''
        approach in reverse; pointer at end, decrement as we step down to see if we can reach it 
        '''
