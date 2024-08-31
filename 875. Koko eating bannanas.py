class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = max(piles)

        left = 1
        right = max(piles)

        while left <= right:
            k = (right + left) // 2 # current k value we are checking

            # find her total eat time @ k valued aat mid
            calcEatTime = 0
            for pile in piles:
                calcEatTime += math.ceil(pile / k)
            
            #print(calcEatTime)
            if calcEatTime <= h:
                # case where we have a valid k
                result = min(result,k)
                right = k - 1
            else:
                # case where RPH is not enough (NOT VALID)
                left = k + 1
        
        return result


        
'''
k, if its more than whats in pile, we round up the hour

we can never take more than h hours to eat the piles

- we want minimum k (ie slowest possible rate to eat all piles)

brute force =  max(n) * n

k = [1,2,3,4,5,6,7...11]
use binary search, we can get max(n) --> log(n)

start with 6; for input [3,6,7,11]
to eat: 0.5 -> 1, 6/6 = 1, 7/6 = 2. 11/6 = 2
total to eat is 6 hours < 8 VALID

condiitons for pointers
move our right pointer to left of midpoint --> WHEN calcEatTime <= h (8)
    check val we are on in k, against current result and take min
move our left pointer to right of midpoint --> WHEN oppositie ie > h (8)
    we need to increase her rate per hour to get within alloted time frame
'''
