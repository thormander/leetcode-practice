class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0

        left = 0

        hashset = set()

        for right in range(len(s)):
            # handle duplicates
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            
            hashset.add(s[right])

            result = max(result,(right-left)+1)
        
        return result


            



    
'''
longest substring

no repeating characters --> hashset for this

running max for result

"abcabcbb"
  L R
'''
