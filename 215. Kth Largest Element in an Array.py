class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # populate our heap
        for num in nums:
            heap.append(-num) #negative as we need max_heap rather than min
        
        heapq.heapify(heap)

        result = 0
        while k > 0:
            result = - heapq.heappop(heap)
            k -= 1
        
        return result
        

        



'''
k is amount of times we need to pop

can use a heap for this (max heap)

python defaults to min heap so we can negate as we add them in
'''
