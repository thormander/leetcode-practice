class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list) # occurance of character* | word

        for word in strs:
            
            occurance = [0] * 26 # represent occurance for letters, with index as the char

            for char in word:
                # index to char relation
                occurance[ord(char) - ord('a')] += 1


            hashmap[tuple(occurance)].append(word)


        return hashmap.values()


'''
anagrams have exact same character count as another

inefficient, but a starting a point:
    sort the strings and compare them n^2

hashmap -> occurance of character* | word

loop through and get the counts of each string and check if it is in our hashmap
- if it is append the word, otherwise just make a new one

occurance of character* = [0,0,0,...] --> index represents the character (ie. index 0 = a)
    - to relate letter to index, use ord() to convert a letter to its unicode value a-a, b-a, c-a ....
    
'''
