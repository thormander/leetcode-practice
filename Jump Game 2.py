class Solution:
    def jump(self, nums: List[int]) -> int:

        min_jumps = 0

        left = 0
        right = 0

        while right < len(nums) - 1:
            # iterate through each section
            max_jump = 0
            for i in range(left,right+1):
                max_jump = max(max_jump,i + nums[i])
            
            left = right + 1
            right = max_jump

            # count as a step after we finish a section
            min_jumps += 1
        
        return min_jumps
            

'''
[{2},{3,1},1,4]
  |   +1

section = index right after the current --> furthest index we can jump to

[{2},{3,1},{1,4}]
  0   +1    +1

result would just be amount of steps taken

for the sections,
use 2 pointers to denote the window
** we know when right pointer reaches last element, we stop counting steps and return **


'''
