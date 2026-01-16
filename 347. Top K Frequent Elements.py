class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsToCount = {}

        # populate our dictionary
        for num in nums:
            if num not in numsToCount:
                numsToCount[num] = 1
            else:
                numsToCount[num] += 1

        # dict --> heap
        heap = []

        for key,value in numsToCount.items():
            heap.append((-value,key))

        heapq.heapify(heap)

        # get max val and go up to k
        result = []

        for i in range(k):
            value, key = heapq.heappop(heap) # value is negative
            result.append(key)
        
        return result



'''
k = top most frequent numbers 

count of each num --> track this

dictionary --> key: num  value: count

[1,1,1,2,2,3]. k = 2
        |
{1:3,2:2,3:1} --> we have to sort to get max

we need a heap --> consistently grabbing the max
 -- so instead of dict, use list and append tuples --> heapify

python defaults heap --> min heap, but we need MAX so negate all values

'''
