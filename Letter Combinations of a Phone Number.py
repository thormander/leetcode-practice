class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        if digits == "":
            return []

        hashmap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        def backtrack(index,currentString):
            # base case
            if len(currentString) == len(digits):
                result.append(currentString)
                return
            
            for digit in digits[index]:
                for letter in hashmap[digit]:
                    backtrack(index+1,currentString+letter)
        
        backtrack(0,"")

        return result






'''
backtrack 

            " "
        /    |     \
       a     b     c
     d e f  d e f  d e f
'''
