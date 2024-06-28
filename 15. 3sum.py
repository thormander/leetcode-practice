class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i,v in enumerate(nums):
            # check duplicate
            if (i != 0) and (v == nums[i-1]):
                continue # skip this iteration

            left = i + 1
            right = len(nums) - 1

            while left < right:
                # check duplicates again
                if (left != i + 1) and (nums[left-1] == nums[left]):
                    left += 1
                    continue
                elif (right != len(nums) - 1) and (nums[right + 1] == nums[right]):
                    right -= 1
                    continue

                # check sum
                currentSum = v + nums[left] + nums[right]
                
                if (currentSum == 0):
                    results.append([v,nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif (currentSum > 0):
                    right -= 1
                else:
                    left += 1
            
        return results


            

        
'''
X _ _

sort it first, ( we can use 2 pointers to help us)

we first iterate through nums,
get the first number, BUT we must check for duplicates:
    if number before is same, we need to skip.
same goes for other 2.

Break this down essentially into a 2 sum after that first step.

Sorting will let us handle the duplicates
'''
