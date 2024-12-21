class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # base case
        if len(nums) == 0:
            return [[]]
        
        permutations = self.permute(nums[1:]) # holds permutations

        result = []

        for permuation in permutations:
            for i in range(len(permuation)+1):
                cur = permuation.copy()
                cur.insert(i,nums[0])
                result.append(cur)


        return result


        

'''
backtracking

base case:
    we return up empty list if nums is 0

recurse on istelf, and pass nums without index 0:
    after we go down to base case, we start adding to a list


1,2,3 
2,3.   [[2,3],[3,2]]
3.    [[3]]
_.  - [[]]

we only add the first index as we go up.
'''
