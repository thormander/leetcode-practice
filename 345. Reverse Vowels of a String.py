class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])

        # 1st pass
        vowels_present = []
        for char in s:
            if char in vowels:
                vowels_present.append(char)

        # 2nd pass
        end = len(vowels_present)-1
        s_list = list(s)
        for i,v in enumerate(s_list):
            if v in vowels:
                s_list[i] = vowels_present[end]
                end -= 1
        
        return "".join(s_list)





'''
set holding our vowels (lowercase and cap)

scan s and add to a new list the vowels present

scan s again, as we go through put a pointer at end of new list holding vowles present and take from end
, decrement as we go
'''
