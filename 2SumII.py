class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l <= r:
            curr_sum = numbers[l] + numbers[r]
            # base case
            if curr_sum == target:
                return [l+1,r+1]
            
            # conditions
            if curr_sum > target:
                r -= 1
            else:
                l += 1
        
        
        '''
        2 pointers; on right and left

        add them together,
            # base case to return when we get == to target
            
            if greater than target:
                decrement our right pointer
            else:
                increment our right pointer
        '''
