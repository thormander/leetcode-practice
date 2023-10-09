class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        # recusive function
        def backtrack(index,subset):
            # base case
            if index == len(nums):
                result.append(subset.copy())
                return

            # recusive call including index
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()

            # recursive call at subsets other than index (handle skipping also)
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index + 1, subset)
        
        backtrack(0, [])
        return result





        '''
        backtrack; make sure to skip over any duplicate numbers
        '''
