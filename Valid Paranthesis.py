class Solution:
    def isValid(self, s: str) -> bool:

        valid = {')':'(', '}':'{',']':'['}
        
        stack = []

        for char in s:
            # case of closing
            if char in valid:
                if stack and stack[-1] == valid[char]:
                    stack.pop() # valid pair
                else:
                    return False
            # case of open
            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False
            


        '''
        make a dictionary: store the pairs of parantheses where a close correposnds to open
        '''
