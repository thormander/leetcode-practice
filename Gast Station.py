class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result = 0
        
        # base case
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                result = i + 1# current station doesn't work so set to next
            
        return result
        

            

        
        '''
        greedy, keep a running total, if its negative, reset to 0 and look at next
        return whenever we get a positive total because that must be the starting point (ie if we skip we will not have   enough to complete it given overall gas is greater than overall cost)
        '''
