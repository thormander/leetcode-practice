class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        left = 0
        right = 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                val = prices[right] - prices[left]
                result = max(result,val)
            
            right += 1
        
        return result


        

'''
maximize profit -> running max variable for result

2 pointer

[7,1,5,3,6,4]
   L       R

p[R] - p[L] = profit

set left = right when it is greater than
otherwise, increment r
'''
