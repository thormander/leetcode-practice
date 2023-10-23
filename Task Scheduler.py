class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        queue = deque() # [amount of chars, time until free]
        maxheap = []

        # count occurances of chars (hashmap) and add to maxheap
        occurances = Counter(tasks)
        for val in occurances.values():
            maxheap.append(-val)
        
        # create the heap (psuedo max heap)
        heapq.heapify(maxheap)

        while maxheap or queue:
            time += 1
            
            if maxheap:
                newOccur = 1 + heapq.heappop(maxheap) # performing 'x - 1' operation as we negated
                if newOccur != 0:
                    # add to queue when non-zero
                    queue.append([newOccur,time + n])
            
            # case when char can be used again
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap,queue[0][0])
                queue.popleft()
        
        return time
        


                        

        '''
        use a max heap; (psuedo max heap)

        use queue to store any tasks that are in timeout
            - do not add when done with chars

        run time counter; eventually return that at the end
        '''
