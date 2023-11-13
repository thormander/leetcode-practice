class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {} # key: letter occurances | value: list of words

        # counts
        for string in strs:
            count = [0] * 26 # represent alphabet (think of index as the letter)
            
            # go through char in the word
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            
            if tuple(count) in hashmap:
                hashmap[tuple(count)].append(string)
            else:
                hashmap[tuple(count)] = [string]
        
        return hashmap.values()


        '''
        map -> key: letter occurances | value: list of words

        list size of 26 (represent our possible characters)
            do the count
            if not in map, put it in with the current word
            if it is, just add the word to the list
        
        return our map.values()

        '''
