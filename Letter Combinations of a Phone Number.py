class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nToL = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = []

        # backtracking
        def backtrack(i,cur_s):
            # base case
            if len(cur_s) >= len(digits):
                result.append(cur_s)
                return
            
            for char in nToL[digits[i]]:
                backtrack(i+1,cur_s + char)
        
        if digits: 
            backtrack(0,"")
        else:
            return []
        
        return result

