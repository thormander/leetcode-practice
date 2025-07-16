class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {} # key: 'letter' | value: occurance
        hashmap_t = {} # key: 'letter' | value: occurance

        len_s = 0
        len_t = 0
        # loop through s
        for char in s:
            len_s += 1
            if char in hashmap_s:
                hashmap_s[char] += 1
            else:
                hashmap_s[char] = 1

        # loop through t
        for char in t:
            len_t += 1
            if char in hashmap_t:
                hashmap_t[char] += 1
            else:
                hashmap_t[char] = 1        

        # make sure they are same size
        if len_s != len_t:
            return False
        
        # compare
        return hashmap_s == hashmap_t

'''
count the occurances of each of the letters

we can compare the counts

2 hashmaps --> key: 'letter' | value: occurance

loop through both s & t (immeadatly return false if not equal length):
    fill up their respective hashmap

compare the hashmaps
'''
