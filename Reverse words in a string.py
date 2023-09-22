class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split() # get words by themselves

        return " ".join(reversed(words))


        '''
        need to split string to individual words -> list

        reverse the list, then .join it on a " "
        '''
