class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            # first check for presence
            if num in hashset:
                return True
            
            hashset.add(num)
        
        return False
