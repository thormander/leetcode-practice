class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums) # first add to a set
        longest = 0

        for num in nums:
            # skip any non starting nums of a sequence
            if (num - 1) in hashset:
                continue
            
            #start of a subsequence
            currentLength = 1
            curr = num
            while (curr + 1) in hashset:
                currentLength += 1
                curr += 1
            
            longest = max(longest,currentLength)
        
        return longest

'''
figure out if we are at the start of a sequence or not
- curreent number we are on, check if there is one to its left (ie. we want to check if there is one less)
- if we are not on current...skip

otherwise
if we are, we can start the longest subsequence count.

use a hashset
'''
