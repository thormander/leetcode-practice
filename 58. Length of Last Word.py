class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0

        for i in range(len(s)-1,-1,-1):
            if result > 0 and s[i] == " ":
                return result
            
            if s[i] != " ":
                result += 1
        
        return result

'''
since we only need last word,
lets just go in reverse

"   fly me   to   the moon  "
                           |

if we have a value in result and hit a " " just return what we have
'''
