class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num-1 not in numSet: #sequence start
                length = 0
                while (num+length in numSet):
                    length += 1
                if length > longest:
                    longest = length
        
        return longest
                



        '''
        put nums into a set
        seqlengths = []
        
        for num in numset
            sequence start if elemenet - 1 is not in set
            if it isn't seqeuce start:
                length = 0
                while (length + n #current number) in numSet:
                    length += 1
                seqLengths.append(length)
        
        return max(seqlengths)

                
        '''
