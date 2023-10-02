class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = [] 
        def DFS(index):
            # base case (where we hit leaf node)
            if index >= len(nums):
                result.append(subset.copy()) # append whatever is in the subset variable (must use copy as variable can be changed later)
                return
            
            # case to include nums[i]
            subset.append(nums[index])
            DFS(index + 1)

            # case not to
            subset.pop()
            DFS(index + 1)
    
        DFS(0)
        return result
