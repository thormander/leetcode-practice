class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []

        minheap = []
        for point in points:
            d = (point[0]-0)**2 + (point[1]-0)**2
            minheap.append([d,point[0],point[1]])
            
        # add to minheap
        heapq.heapify(minheap)
        
        # add to result
        count = 0
        while count != k:
            d,x,y = heapq.heappop(minheap)
            result.append([x,y])
            count += 1
        
        return result

        
        '''
        calc distance for each point, just add distance to front of coord list;

        use min heap
        '''
