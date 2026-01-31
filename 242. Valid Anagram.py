class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # populate our maps with counts
        s_map = self.populate_helper(s) 
        t_map = self.populate_helper(t)

        # compare
        return s_map == t_map

    def populate_helper(self,string: str):
        hashmap = {} # key: char | value: occurances
        
        for char in string:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        return hashmap

'''
count each of the letters from both strings
    - use dictionary to track letter to count
    - if both dictionaries same, return true

1. populate map for both s and t
2. compare the maps
'''
