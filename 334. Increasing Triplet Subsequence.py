class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float('inf')

        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                # we found a k, therefore treu
                return True
        
        return False

'''
     j i 
[2,1,5,0,4]

left --> right should hold true for i < j < k
check if num less than current i, then j

return True, k needs to be larger than j
'''
