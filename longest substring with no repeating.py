class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()

        left = 0
        right = 0

        result = 0

        while right < len(s):
            # handle duplicate
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            # check length
            result = max(result,(right-left)+1)

            hashset.add(s[right])
            right += 1
        
        return result
            


'''
sliding window
"abcabcbb"
 lr

hashset to check for duplicates
'''
