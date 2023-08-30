class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequencies = [[] for i in range(len(nums)+1)]
        result = []

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1 # incrementing
        for key,value in hashmap.items():
            frequencies[value].append(key)

        for i in range(len(frequencies)-1,0,-1):
            for num in frequencies[i]:
                result.append(num)
                
                if len(result) == k:
                    return result




        '''
        hashmap: key is numver --> value is occurences

        declare an array to the length of nums (index will correspond to occurences)
        - +1 because 0 occurences or index doesnt count

        loop for finding occurences

        loop for adding the hashmap of occurences to array

        loop in reverse to find the max occurences:
            loop againg to access the sublist
                add the first encounter to a result array

                 check if we hit 'k' when length of result arrary is equal 
        '''
