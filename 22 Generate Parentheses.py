class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = [] # for building combinations
        
        results = [] # store all combinations

        def recurse(amountOpen,amountClosed):
            # base case
            if n == amountOpen == amountClosed:
                results.append("".join(stack))
                return
            
            # case: only add open pars when its less than n
            if amountOpen < n:
                stack.append('(')
                recurse(amountOpen + 1,amountClosed)
                stack.pop()

            # case: only add closing pars when amountClosed less than amountOpen
            if amountClosed < amountOpen:
                stack.append(')')
                recurse(amountOpen,amountClosed + 1)
                stack.pop()

        
        recurse(0,0)
        return results

    '''
    stack to track our parenthese being built

    need to track amount open and closed
     - n = amount max open = amount max clsing pars

     backtracking/recursion to build up the combinations
    '''
