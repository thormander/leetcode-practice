class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = 0
        hashset = set()
        l = 0
        
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            result = max(result, len(hashset))
        
        return result
            


        '''
        2 pointers; use a hashset

        set our l to 0

        for r in s
            check if r in hashset:
                set.remove(l)
                l += 1
            else:
                go ahead and add r to set
            check for max and update our running total


        '''
