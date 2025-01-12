class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        result = []

        def backtrack(index,cur_s):
            # base case
            if len(digits) == len(cur_s):
                # we know we found one
                result.append(cur_s)
                return
            
            for char in hashmap[digits[index]]:
                backtrack(index+1,cur_s + char)
            
        backtrack(0,"")

        if digits == "":
            return []
        else:
            return result


'''
"23"

      2
|      \          \
a       b          c
| \ \   | \ \      | \ \
d  e f  d  e f     d  e f
'''
