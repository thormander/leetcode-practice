class Solution:
    def isValid(self, s: str) -> bool:

        valid_pars = {"]":"[",")":"(","}":"{"}
        stack = []

        # edge case
        

        for char in s:
            if not stack and char in valid_pars.keys():
                return False

            if char in valid_pars.keys() and stack[-1] == valid_pars[char]: # closed 
                stack.pop()
            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False



'''
"...()[]{}"
         |
[]

map where we have pairs of parenthesis
    - searching on closing, we use closing pars as key

stack ds --> last in first out
 - keep track of our current paraentheis
 - pay attention to closing parenthees

once we hit end, if stack is not empty --> return false because it means at least one par was not closed
'''
