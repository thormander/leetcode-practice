class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # base case
        if len(hand) % groupSize != 0:
            return False
        
        countMap = {} # number : occurances
        # populate our map
        for num in hand:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        
        # populate heap
        minHeap = list(countMap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            minNum = minHeap[0]

            for i in range(minNum, minNum + groupSize): # what we expect the sub group to be
                # case when it doesn't work
                if i not in countMap:
                    return False
                countMap[i] -= 1

                # remove from minheap if 0
                if countMap[i] == 0:
                    if i != minHeap[0]:
                        return False # result in out of order pop, return false
                    heapq.heappop(minHeap)
        
        return True
                
        

        
        '''
        min heap; keep a map for counts
            pop from our minHeap when occurances hits 0

        False?
            whenever we try to pop a number that isn't the min
            if it is impossible to be divided evenly
        '''
