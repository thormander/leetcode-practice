class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # key: number | value: occurance

        # get counts
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        # bubble sort list and populate
        bubble = [[] for i in range(len(nums)+1)]

        for key,val in hashmap.items():
            bubble[val].append(key)
        
        
        # iterate in reverse and get result
        result = []

        for i in range(len(bubble)-1,0,-1):
            for num in bubble[i]:
                result.append(num)
                if len(result) == k:
                    return result
                



'''
bubble sort
 - indexes represent the occurance

 [1,1,1,2,2,3]


 [0,1,2,3,4,5,6]. --> [[],[3],[2],[1],[],[],[]]
  _ _ _ _ _ _ _

 3: [1,3]
 2: [2]
 1: [3]

get counts of each number --> hashmap

make our bubble sort list

go in reverse to get the top k on our bubble sort array
'''
