class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1) # just setting max amount

        # base case
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i],1 + dp[i - coin])
        
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
        

        '''
        fewest amount; if nothing, then -1
        '''
