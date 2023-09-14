class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {} # key: 'char' | value: occurances
        result = 0

        l = 0
        for r in range(len(s)):
            # add/update char to dict
            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
            
            while (r-l+1) - (max(hashmap.values())) > k: # this is length of window - most freq character
                hashmap[s[l]] -= 1
                l += 1
            result = max(result,(r-l+1))
        
        return result
