class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # base case
        if len(prices) == 1:
            return 0

        result = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                candidate = prices[right] - prices[left]
                result = max(result,candidate)
            right += 1

        
        return result

'''
2 pointers

if val@left > right:
    set left = right
    right += 1
else:
    right - left value
    check on a running max

[7,1,5,3,6,4]
   | |
'''
