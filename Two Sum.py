class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # key: value | value: index

        for i,v in enumerate(nums):
            check = target - v
            # base case (ie. check if we have an answer)
            if check in hashmap:
                return [i,hashmap[check]]

            hashmap[v] = i




        
'''
change nums to a hashmap

value = target - current number
    - is this value in our set

return indeces, so store as a pair (index,value)
'''
