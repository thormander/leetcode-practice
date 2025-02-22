class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        top = 0 # word 1
        bot = 0 # word 2

        while top < len(word1) and bot < len(word2):
            # do the alternations
            result += word1[top]
            top += 1

            result += word2[bot]
            bot += 1
        
        # handle remaining letters
        if len(word1) > len(word2):
            # append rest of word 1
            result += word1[top:]
        else:
            result += word2[bot:]
        
        return result

'''
result = ""

just alternate, start with word 1

stop alterating as soon as we run out of length for one of them

jsut append the rest to result for longer one

2 pointers one on word1 and one on word2
'''
