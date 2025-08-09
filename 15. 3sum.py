class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        left = 0 # primary

        # 1. sort input
        nums.sort()

        while left < len(nums):
            # make sure left is not same as previous 
            if left != 0 and (nums[left] == nums[left-1]):
                left += 1
                continue

            middle = left + 1
            right = len(nums) - 1

            while middle < right:
                cur_sum = nums[left] + nums[middle] + nums[right]

                # check against cur_sum
                if cur_sum > 0:
                    right -= 1
                elif cur_sum < 0:
                    middle += 1
                else:
                    result.append([nums[left],nums[middle],nums[right]])

                    # also skip duplicates for these 2
                    while middle < right and (nums[middle] == nums[middle+1]):
                        middle += 1
                    while middle < right and (nums[right] == nums[right-1]):
                        right -= 1
                    
                    middle += 1
                    right -= 1
            
            left += 1
            
        return result
            

'''
[-1,0,1,2,-1,-4]
[-4,-1,-1,0,1,2] -> sorted
        |
           |
              |

3 pointers
-4 --> 0
add our poitners
    if its > 0:
        decremetn the right pointer
    if its < 0:
        incremetn the middle pointer
    else
        add to result list
    

sort it first so we can do it similar to 2 sum

need to skip any same numbers @ all pointers
'''
