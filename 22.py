class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        tempStack = []

        def recurse(amountOpen,amountClosed):
            #base case
            if amountOpen == amountClosed == n:
                result.append("".join(tempStack))
                return
            
            # deal with open
            if amountOpen < n:
                tempStack.append("(")
                recurse(amountOpen+1,amountClosed)
                tempStack.pop()
    
            # deal with closed
            if amountClosed < amountOpen:
                tempStack.append(")")
                recurse(amountOpen,amountClosed+1)
                tempStack.pop()
        
        recurse(0,0)
        return result



        '''
        n pairs --> n open and n closed 

        use a stack for result
        stack for temporary use

        1. we need an open p before adding a closed ie. amount closed < amount open
        2. open p's < n in order to add
        3. valid combination if n == amount open == amount closed. -- base case

        need to do recursion, pass amount open and closed
        '''
