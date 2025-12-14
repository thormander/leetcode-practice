class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        result = 0
        left = 0
        right = 1

        while right < len(prices):
            # first calc current profit
            profit = prices[right] - prices[left]
            result = max(result,profit)

            # second update pointers
            if (prices[left] > prices[right]):
                left = right
            
            right += 1


        return result     

'''
result = running max

left @ index 0
right @ index 1

shift left to right if its less, and increase right by 1




'''
