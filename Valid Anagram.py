class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {} # key: letter | value: occurances
        mapT = {}
        
        # populate mapS
        for char in s:
            if char not in mapS:
                mapS[char] = 1
            else:
                mapS[char] += 1
        
        # populate mapT
        for char in t:
            if char not in mapT:
                mapT[char] = 1
            else:
                mapT[char] += 1
        
        return mapS == mapT
        
        '''
        using more space -> use map an count character occurances
        O(n)
        '''
