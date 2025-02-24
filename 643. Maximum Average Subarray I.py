class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        current_sum = 0
        #1. build up our initial window
        for i in range(0,k):
            current_sum += nums[i]
        
        result = current_sum / k

        # 2. slide window
        for i in range(k,len(nums)):
            current_sum -= nums[i-k]
            current_sum += nums[i]
            result = max(result,current_sum / k)
        
        return result
        


'''
window length k

calc that avg and keep track of a running max

instead of recalcing avg everytime, we do it as we move window, so subtract out number that was left out
add new one in and recalc avg

1. create the initially sized window up to k
- create avg
2. slide window
    - remove leftmost number
    - add in new number to the right of window
    - update result average
'''
