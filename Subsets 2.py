class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(index,subset):
            # base case
            if index == len(nums):
                result.append(subset.copy())
                return
            
            # decision left
            subset.append(nums[index])
            backtrack(index+1,subset)

            # decision right
            subset.pop() # bring back to original state
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1,subset)
        
        backtrack(0,[])
        return result


    

'''
backtracking
we also need to sort the input

decision tree
    - left include the current number
    - right don't include (BUT if next number is same, we need to skip it)

function backtrack(index, some list):
    base case
        - index is at the end of the list, add to our result list
    
    recursion left
    

    recursion right
        - skip any numbers that are initially the same as current index
        - make sure to pop to undo (as we are skipping the number)
    
'''
