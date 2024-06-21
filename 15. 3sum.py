class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i,v in enumerate(nums):
            # check duplicate
            if ((i > 0) and (nums[i-1] == v)):
                continue # skip
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = v + nums[left] + nums[right]
                # base case
                if currentSum == 0:
                    output.append([v,nums[left],nums[right]])
                    left += 1
                    right -= 1

                    # check duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1

                elif currentSum > 0:
                    right -= 1
                else: # we are less than 0
                    left += 1
            
        return output          
            



'''
incoporate 2sum with poiters (sorted)
sort first then oslve with pointers
_ +  _ +  _ == 0

avoid duplicates
    - in our iteration, if we are the same as previous, then skip
'''
