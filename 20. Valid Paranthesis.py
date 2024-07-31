class Solution:
    def isValid(self, s: str) -> bool:
        reference = {')':'(','}':'{',']':'['}

        stack = []

        for char in s:
            # check if open
            if char in reference.values():
                stack.append(char)
            else: # when we hit a closing
                if (stack) and (reference[char] == stack[-1]):
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False



'''
know the pairs --> dictionary/map key: *closing* | value: *opening*

iterate through
 - stack...add opens to it
 - when we hit a closing --> check top of stack and compare to value in map.
 - if equal remove from stack
 - otherwise, return False

if our stack is empty --> reutrn true 
'''
        
