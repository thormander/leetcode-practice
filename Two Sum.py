class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # num : index

        for index, num in enumerate(nums):
            check = target - num

            if check in hashmap:
                # find a valid pair
                return [hashmap[check],index]
            
            # otherwise just add to our map
            hashmap[num] = index
        


        '''
        map -> num : index

        use target - num to check in map

        '''
