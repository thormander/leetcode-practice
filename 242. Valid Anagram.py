class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {} # key: char | value: occurances
        hashmap_t = {}

        # S
        for char in s:
            if char in hashmap_s:
                hashmap_s[char] += 1
            else:
                hashmap_s[char] = 1

        # T
        for char in t:
            if char in hashmap_t:
                hashmap_t[char] += 1
            else:
                hashmap_t[char] = 1
        
        return hashmap_s == hashmap_t


'''
dictionary --> key: char | value: occurances

get occurances of both and see if they are equal
'''
