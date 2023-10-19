class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float("inf")] * (amount + 1)
        cache[0] = 0 # base case
        
        for cur_amount in range(1,amount+1):
            for coin in coins:
                # valid coin ?
                if (cur_amount - coin) > -1:
                    cache[cur_amount] = min(cache[cur_amount], 1 + cache[cur_amount - coin])
        
        if cache[amount] != float("inf"):
            return cache[amount]
        else:
            return -1




        '''
        DP - bottom up; determine how to get to amount of 0,1,2...amount
        need a cache - amount + 1 (cover from 0 -> amount inclusive)

        valid if amount - current coin is non negative
        '''
