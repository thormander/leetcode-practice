class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        result = 0

        for num in hashset:
            # if it is start
            if num - 1 not in hashset:
                seqLength = 0
                temp = num
                while temp in hashset:
                    seqLength += 1
                    temp += 1
                result = max(result,seqLength)
            else:
                continue
        
        return result
            

        
        '''
        subsequence? --> if num - 1 is in nums, then that is not start
            if it isn't then we have the start of a subsequence, we can count length

        USE A SET!!! --> takes too long otherwise
        '''
