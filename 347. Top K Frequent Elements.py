class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # get counts of the numbers
        count = {} # key: number | value: occurances
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # start making heap
        heap = []
        for num in count.keys():
            heapq.heappush(heap,(-count[num],num))
        
        
        # grab top k
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

        
'''
most frequent --> heap (max)

make the heap based on occurance of each num

(frequency,number)

create heap based of frequency

heap pop to get k most (BUT --> negate all the frequencies to get a 'max-heap')
'''
