class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # check if mid is target
            if target == nums[mid]:
                return mid


            # left sorted portion
            if nums[mid] >= nums[left]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums [right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1    

'''
logn --> sorts --> binary search

[4,5,6,7,0,1,2]
 |
             |

while the pointers arent croseed
    base, check if are section is sorted (is left < right)

    find mid (and check if its target)
    
    if mid > left AND target >= left
        search left
    
    else
        search right

'''
