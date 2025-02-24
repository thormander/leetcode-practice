class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_right = sum(nums) # start with sum since we are all the way left initially
        total_left = 0

        for i,v in enumerate(nums):
            # can't include pivot
            total_right -= v

            # compare
            if total_left == total_right:
                return i
            
            # add pivot to left
            total_left += v
        
        return -1

'''
[1,2,3] 
   |

total_right = 6 - 1 = 5 - 2 = 3 - 3 = 0
total_left = 0 + 1 = 1 + 2 = 3// after the comparison

leftmost pivot

don't include the pivot in sum

- find sum of whole list first
- go through list
- subtract current num from total_rigth
- compare total left vs total right
- increment total_left with num on pivot
'''
