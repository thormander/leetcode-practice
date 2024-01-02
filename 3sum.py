class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i,v in enumerate(nums):
            # handle duplicates
            if i > 0 and nums[i-1] == v:
                continue

            # 2 pointer method
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = v + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([v,nums[left],nums[right]])
                    # update pointers / handle duplicate
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return result
                    

        '''
        sort nums first --> allows us to use 2 pointers
            apply 2 sum to 3 sum
        

        '''
