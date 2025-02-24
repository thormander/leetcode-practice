class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0 

        result = 0 # track max window size

        # build up our window as big as possible
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
               zeros += 1

            while zeros > k:
                # shrink window from left up until we are within k
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            right += 1

            result = max(result,right-left) # pot. candidate

        return result

'''
sliding window
constantly increase size up as long as our number of 0's are <= k

if we reach the k, then record size of window

slide the window
keep track of how many 0's are added/removed
'''
