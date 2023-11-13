class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # num : occurance
        
        # set up our bucket sort
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        

        # count occurances
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        # add values to our bucket
        for key, value in hashmap.items():
            bucket[value].append(key)
        
        result = []

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
            
            if len(result) == k:
                return result
            
            
        

        '''
        map for counts

        bucket sort -> where index represents occurances and value is the actual number
        '''
