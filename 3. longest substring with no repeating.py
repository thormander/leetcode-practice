class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = 0
        left = 0
        right = 0
        hashset = set()

        while right < len(s):
            # update our window/hashset    
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1

            hashset.add(s[right])
            result = max(result,len(hashset))
            right += 1
            
        
        return result


'''
set (track if a letter we are going to add to our windows is valid)
set is our window

2 pointers:
left = 0 right = 0

intilize set with those 2,
shift left pointer when thers a duplicate (which will be added via right pointer)
'''
