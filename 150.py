class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                top, nextTop = stack.pop(), stack.pop()
                res = nextTop + top
                stack.append(res)
            elif char == '-':
                top, nextTop = stack.pop(), stack.pop()
                res = nextTop - top
                stack.append(res)
            elif char == '*':
                top, nextTop = stack.pop(), stack.pop()
                res = nextTop * top
                stack.append(res)
            elif char == '/':
                top, nextTop = stack.pop(), stack.pop()
                res = int(nextTop / top)
                stack.append(res)
            else:
                stack.append(int(char))
        
        return stack[-1]


        '''
        use a stack

        loop through tokens:
            if +
                pop top 2 and add
                append the result
            if -
                pop top 2 and minus
                append the result
            if *
                pop top 2 and multiply
                append the result
            if /
                pop top 2 and divide
                append the result

            add char to stack
        
        return stack[-1]
        '''
