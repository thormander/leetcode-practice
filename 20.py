class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reference = {")":"(","]":"[","}":"{"}

        for char in s:
            if char in reference: # encountered closing bracket
                if stack and reference[char] == stack[-1]:
                    stack.pop() # found a valid pair
                else:
                    return False
            else:
                stack.append(char)
        
        if not stack:
            return True # stack is empty
        else:
            return False

        

        '''
        every closing bracket must have an open
        -- > use dictionary/hashmap to have pairs for corresponding to each other

        for loop through
            use a stack; pop whenever we find a valid pair
            append otherwise


        -- if its empty we can consider that True
        -- if not then it is false
        '''
