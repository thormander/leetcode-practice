class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        hashmap = {} # key: character | value: occurance

        left = 0

        for right in range(len(s)):
            # update occurances
            if s[right] not in hashmap:
                hashmap[s[right]] = 1
            else: 
                hashmap[s[right]] += 1
            
            # logic for our left pointer and make sure our window is valid
            while ((right - left + 1) - max(hashmap.values())) > k:
                hashmap[s[left]] -= 1
                left += 1
            
            result = max(result, (right - left + 1))
        
        return result

         

'''
2 pointers --> sliding window

keep track of character counts --> hashmap key:char value: occurances

left pointer...

"ABAB"
 L  R
 window size
(R - L) + 1 - max(hashmap occurances) = 4 - 2 = 2 <= k

A: 2
B: 2

increment left with while loop until we get within the k again.
    - also need to make sure we update counts as we do this.

'''
