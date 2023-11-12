class Solution:
    def checkValidString(self, s: str) -> bool:
        pLeft = 0
        pMax = 0

        for char in s:
            if char == '(':
                pLeft += 1
                pMax += 1
            elif char == ')':
                pLeft -= 1
                pMax -= 1
            else: # case of '*'
                pLeft -= 1
                pMax += 1
            
            if pMax < 0:
                return False
            
            if pLeft < 0:
                pLeft = 0
            
        return pLeft == 0
