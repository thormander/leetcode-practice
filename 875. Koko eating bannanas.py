class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = result = max(piles)

        while left <= right:

            current_speed = (left + right) // 2 # midpoint
            
            time_to_eat = 0

            for pile in piles:
                time_to_eat += math.ceil(pile / current_speed)
            
            if time_to_eat <= h:
                result = current_speed
                right = current_speed - 1
            else:
                left = current_speed + 1
    
        return result

'''
minimum k

binary search on k or eating speed

0,1,2,3...max(piles)

1,2,3,4,5,6,7,8,9,10,11
|
                      |

'''
