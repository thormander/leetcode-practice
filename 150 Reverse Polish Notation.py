class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = set(["+","-","*","/"])

        stack = []

        for char in tokens:
            # number?
            if char not in operators:
                stack.append(char)
            else:
                # pop the top 2 nums
                numR = int(stack.pop())
                numL = int(stack.pop())

                # it is an operator
                if char == "+":  
                    stack.append(str(numL + numR))
                
                if char == "-":
                    stack.append(str(numL - numR))

                if char == "*":
                    stack.append(str(numL * numR))

                if char == "/":
                    stack.append(str(int(numL / numR)))

        return int(stack[0])
'''
tokens = ["2","1","+","3","*"]
                           |

stack [9]

hit "+"
    pop 2 times
    add those 2 numbers
    add back in stack


use a stack

any time we see a operator, take the prev 2 numbers (on the stack) and do the operation
'''
