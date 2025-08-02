class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_sequence = 0
        
        # loop through nums and find if its a starting number of a sequence
        for num in hashset:
            if (num - 1) not in hashset:
                current_sequence_length = 1
                temp = num
                while temp + 1 in hashset:
                    current_sequence_length += 1
                    temp += 1
                
                longest_sequence = max(longest_sequence,current_sequence_length)
        
        return longest_sequence

                



'''

[100,4,200,1,3,2]
           |
set = [100,4,200,1,3,2]
longest = 1

how do we know we are at the start of a sequence --> in the set, there is no number on the (current num - 1)

if we are at start:
    track current length
    while num+1 is in the set, keep incrementing

    compare longest to current length
'''
