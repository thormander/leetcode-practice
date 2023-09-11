class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = right

        while left <= right:
            mid = (right + left) // 2
            amountH = 0
            
            # go through piles and calc amount hours it will take
            for pile in piles:
                amountH += math.ceil(pile / mid)
            
            if amountH <= h:
                k = min(mid,k)
                right = mid - 1
            else:
                left = mid + 1
        
        return k



        '''
        k = bph ;  need to find how many bph koko must eat to finish before guards get back

        k can be a value from 1,2,3,...max of piles
            treat like a list, do binary search on it

            if the mid is not enough bph:
                need to go search right
            else mid enough:
                update our k
                search left for possible smaller value
        


        return min of k within h hours
        '''
