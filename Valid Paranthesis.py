class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(','}':'{',']':'['}

        for char in s:
            # base case
            if not stack and char in hashmap:
                return False
            
            if stack and char in hashmap and stack[-1] == hashmap[char]:
                stack.pop()
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True
         
        '''
         a stack; (remove complete pairs)
         map -> store the corresponding pair

         we know if its true, then there should not be anything in the stack
         '''
