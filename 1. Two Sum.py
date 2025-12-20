class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} # key: num, value: index

        for i,v in enumerate(nums):

            check = target - v

            if check in dictionary:
                return [i,dictionary[check]]
            else:
                dictionary[v] = i

        

'''
returning the INDEXes

[2,7,11,15] target = 9
 | 

target - current num --> is this in our set? 
    - YES, return indexes
    - NO, do not return
'''
