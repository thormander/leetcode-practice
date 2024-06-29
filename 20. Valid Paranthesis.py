class Solution:
    def isValid(self, s: str) -> bool:
        compliments = {")":"(","}":"{","]":"["}
        stack = []

        for char in s:
            if (not stack) and (char in compliments.keys()):
                return False
            
            # case we have opening, then just add to stack
            if (char in compliments.values()):
                stack.append(char)
            elif (stack[-1] == compliments[char]):
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        else:
            return False



'''
use a stack to store incoming chars,

as we close them, remove from stack
'''
