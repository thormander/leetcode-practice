class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        right = 0
        result = 0
        
        while right < len(s):
            # handle our hashamp (what chars and how many in window)
            if s[right] not in hashmap:
                hashmap[s[right]] = 1
            else:
                hashmap[s[right]] += 1
            
            # keep removing chars from left until our window is valid again (within k diff chars)
            while (right-left+1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1

            result = max(result,sum(hashmap.values()))

            right += 1

        return result

'''
hashmap key: char | value: occurance
    represents what is in our window

running max result

left,  right = 0
'''
