class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # base case
        if sum(gas) < sum(cost):
            return -1
        
        station_p = 0
        tank = 0
        for i in range(len(gas)):
            net = gas[i] - cost[i]
            tank += net

            if tank < 0:
                tank = 0
                station_p = i + 1

        return station_p



'''


base case
 we have at least gas >= cost

[1,2,3,4,5], gas
[3,4,5,1,2] cost
[-2,-2,-2,3,3] net
          |
Tank = 6
'''
