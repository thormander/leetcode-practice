class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [] # hold our T/F's
        
        maxCandy = max(candies)

        for candy in candies:
            if candy + extraCandies >= maxCandy:
                result.append(True)
            else:
                result.append(False)
        
        return result
        


'''
find the max in candies

one more scan to check if we give all the extra it passes the max
    if it does true, else false
'''
