class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            # should be same pattern (ie. we dont get 2 unrelated strings)
            gcd = math.gcd(len(str1),len(str2))
            return str1[:gcd]
        
        return ""
'''

check if they are actually similar patterns
    str1 + str2 == str2 + str1 --> should return true if same pattern

take gcd of the lengths of each string

return one of the strings up to length of our gcd
'''
