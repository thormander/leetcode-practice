class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #  key: num | value: index

        for i,v in enumerate(nums):
            # check if we can hit target
            check = target - v 

            if check in hashmap:
                return [i,hashmap[check]]
            
            hashmap[v] = i
        


        


'''
nums = [3,2,4], target = 6
            |
hashmap --> key: num | value: index
'''
