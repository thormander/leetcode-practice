class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap - key: number | value: index
        hashmap = {}

        for i,v in enumerate(nums):
            # check if valid pair
            valid_pair = target - v
            
            if valid_pair in hashmap:
                return [i,hashmap[valid_pair]]
            
            hashmap[v] = i



'''
store elements we have seen
- hashmap

take current element we are on

map - [2]
[2,7,11,15]
   |

 target - current_num --> if this is in our set, we found the 2 numbers

 returning index --> store num with index
'''
