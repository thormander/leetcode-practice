class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)

        for i in range(len(cost)-3,-1,-1): # starting on n-1 term
            cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])


        return min(cost[0],cost[1])

            



        '''
        DP; start at subproblem (add a 0 to the input list)
        - we can consider the final step to be 0
        - work our way from n -> start
        '''
