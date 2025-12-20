class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictionary = {}
        result = []

        for s in strs:
            # get char count
            key = [0] * 26 # represent alphabet

            for char in s:
                i = ord(char)- ord('a')
                key[i] += 1
            
            if tuple(key) not in dictionary:
                dictionary[tuple(key)] = [s]
            else:
                dictionary[tuple(key)].append(s)

        for li in dictionary.values():
            result.append(li)    
        
        return result
        

'''
list of anagram lists

hashmap --> key: list of chars present | value: list of anagrams

count chars -> [0] * 26 letters in alphabet; we increment the index corresponding to letter
    - ord to get indexes of each char/letter
'''
