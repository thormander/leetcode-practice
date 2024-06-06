class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {} # number, occurance

        # get the counts
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        dataStructure = [[] for i in range(len(nums) + 1)]

        # populating our ds
        for num, count in hashmap.items():
            dataStructure[count].append(num)
        
        result = []
        # go in reverse
        for i in range(len(dataStructure) - 1, -1, -1):
            for num in dataStructure[i]:
                result.append(num)
                
                if len(result) == k:
                    return result


        

'''
[1,2,3,4,...]
 1 2 3 ...
 index = our count of number

as we count the frequencies, think of the index as the current frequency
 - hashmap to store the counts

[3, 2, 1]
<-------- loop reverse order k amount increments
'''
