class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # base case, need to have same length
        if len(word1) != len(word2):
            return False
        
        # also, need to have same characters, we cant change them (we could use set, or the keys from hashmap)
        if set(word1) != set(word2):
            return False
        
        # get the counts
        hashmap_1 = {} # key: char | value: count
        hashmap_2 = {}
        for char in word1:
            if char not in hashmap_1:
                hashmap_1[char] = 1
            else:
                hashmap_1[char] += 1

        for char in word2:
            if char not in hashmap_2:
                hashmap_2[char] = 1
            else:
                hashmap_2[char] += 1
        
        if sorted(hashmap_1.values()) == sorted(hashmap_2.values()):
            return True
        else:
            return False

               

'''
word1 = "abca", word2 = "bcab"
a.   2      1
b.   2      1
c.   4      6

- length needs to be same *
- need to have same characters (cant change to a char not in the word) * 
- able to do op2, only if each letter has the same occurances
    - look at one of the words, and check if word 2 has similar occurances
'''
