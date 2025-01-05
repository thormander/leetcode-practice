class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        count = 1
        left = 1
        while left < len(nums):
            if nums[left-1] == nums[left]:
                count += 1

                if count > 2:
                    nums.pop(left)
                    continue
            else:
                count = 1
            
            left += 1
        
        return left


    

'''
in place --> we can only modify the existing input

[1,1,2,2,3]
         |

base case:
    check if length == 1

count = 1
left = 1--> end of list
    nums[left - 1] == nums[left]?
        if it is: count++
        if not: count = 1

        if at any point count > 2:
            pop number at left
            count--
        
return left
'''
