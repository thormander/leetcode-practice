class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones) # psuedo max heap

        while len(stones) > 1:
            # get 2 largest stones
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 == stone2:
                continue
            else:
                smashed = -stone1 + stone2 # values neg, so convert
                heapq.heappush(stones,-smashed)
        
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
