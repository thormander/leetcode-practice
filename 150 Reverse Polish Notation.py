class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+','-','*','/']

        stack = [] # store integers here instead of strings

        for char in tokens:
            if char not in operations:
                stack.append(int(char))
            else:
                last = stack.pop()
                secondlast = stack.pop()

                # logic for each operator
                if char == '+':
                    temp = last + secondlast
                    stack.append(temp)
                elif char == '-':
                    temp = secondlast - last
                    stack.append(temp)                    
                elif char == '*':
                    temp = last * secondlast
                    stack.append(temp)
                else: # division '/'
                    temp = int(secondlast / last)
                    stack.append(temp)
        return stack[-1]


            

        
'''
use stack

[3, 3] *  
'''
