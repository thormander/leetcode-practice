class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # key: [0,0,0...] (26 0's) | value: [nat,tan] 

        for string in strs:
            # do the 26 0's to represent alphabet
            count = [0] * 26
            
            # get occurances
            for char in string:
                position = ord(char) - ord('a')
                count[position] += 1
            
            # add to hashmap
            if tuple(count) in hashmap:
                hashmap[tuple(count)].append(string)
            else:
                hashmap[tuple(count)] = [string]
        
        return list(hashmap.values())




'''
anagram - have exact same letters and letter count

hashmap key: [0,0,0...] (26 0's) | value: [nat,tan] 
    - key holds the alphabet all starting at 0 so we know the occurances

loop:
    fill our hashmap
    do the 26 0's list
    count the letter occurances
        - to match correct index, use ord(current letter) - ord('a')
    
    now we have a key of occurances + a value of the anagram we counted

return the values in our hashmap

'''
