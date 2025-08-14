class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairMap = {')':'(','}':'{',']':'['}

        for char in s:
            if char not in pairMap:
                stack.append(char)
            else:
                if stack and (pairMap[char] == stack[-1]):
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False
        

'''
closing is important!

map a closing bracket --> respective opening bracket

use a stack and just add opening brackets to it

anytime we run into a closing, check the top of our stack to see if it matches the closing (if it is pop the top of our stack)

if after everything, our stack still has something, that means its false

Input: s = "([])"
                |
[]
'''
