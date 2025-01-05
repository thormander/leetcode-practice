class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        result = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[right] > prices[left]:
                result += prices[right] - prices[left] # will give us a pos value
            
            right += 1
            left += 1
        
        return result


'''
just keep adding to our total anytime we have a positive gain between two days

we only hold a stock for at most one day to make it simpler

[7,1,5,3,6,4] 
    | |
[1,2,3,4,5]
       | |
'''
