class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            # first do check
            if num in hashset:
                return True
            
            hashset.add(num)

        # if we dont find any
        return False
    
'''
for loop on nums:
    add each num to a hashset we made
    as we add, just check if its already in there

    if it is --> return true

return false if we get through the entire for loop
'''
