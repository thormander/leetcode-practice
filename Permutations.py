class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base case
        if len(nums) == 1:
            return [nums.copy()]
        
        for i,v in enumerate(nums):
            n = nums.pop(0) # pop first val

            permutations = self.permute(nums) 
            
            # take generate permutations and add to result
            for p in permutations:
                # add n to end
                p.append(n)

            result.extend(permutations)
            nums.append(n)
        
        return result
