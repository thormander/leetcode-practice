class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        result = 0 # longest subarray
        
        cur_zeros = 0 # track how many 0's in our window
        for right,v in enumerate(nums):
            # check if right is a zero
            if v == 0:
                cur_zeros += 1
            
            # check if we have more than 1 zero; shrink if we do
            while left < len(nums) and cur_zeros > 1:
                if nums[left] == 0:
                    cur_zeros -= 1
                left += 1

            # update result with pot. candidate
            # also, account for 'deletion' of the zero, so do not add 1 to acct for size for right-left
            result = max(result,right-left)

        return result

'''
[0,1,1,1,0,1,1,0,1]
   l
         r

cur_zeros = 0

'delete' -> allowance for a 0 in our subarray

we can only have up to 1 zero

window
 - grow window as large as possible
 - 2 pointers
 - keep track of amt zeros in our window, we can only have at most 1
 - shrink window from left if we have more than one zero
 - check if we got a longer subarray
'''1493. Longest Subarray of 1's After Deleting One Element
