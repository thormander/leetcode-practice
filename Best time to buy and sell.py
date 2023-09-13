class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit,profit)
            else:
                l = r

            r += 1
        
        return maxProfit

        '''
        try 2 pointers
        keep them together (side by side)

        r - l = a value. (compare to max)
        if right < left:
            increment left
            increment right
            calculate difference
        else:
            increment right
            calculate difference
        '''
