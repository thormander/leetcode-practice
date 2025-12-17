class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1 = {}
        hashmap_s2 = {} # counts of chars in our window

        # s1 (we can permutate)
        for char in s1:
            if char in hashmap_s1:
                hashmap_s1[char] += 1
            else:
                hashmap_s1[char] = 1
        
        # s2 (where we shift our window)
        maxWindowSize = len(s1)
        left = 0
        right = 0

        while right < len(s2):
            char = s2[right]
            # fill hashmap s2
            if char in hashmap_s2:
                hashmap_s2[char] += 1
            else:
                hashmap_s2[char] = 1

            # make sure our windo is valid size
            while (right - left + 1) > maxWindowSize:
                hashmap_s2[s2[left]] -= 1
                
                # handle case if its occurance is now 0
                if hashmap_s2[s2[left]] == 0:
                    del hashmap_s2[s2[left]]
                
                left += 1

            if hashmap_s1 == hashmap_s2:
                return True
            
            right += 1
            
        return False

'''
2 maps - s1 is our reference, traverse through s2
 key: char | value: occurances

we know its a substring if we run across a window with same dictionary

window will be length of s1
'''
