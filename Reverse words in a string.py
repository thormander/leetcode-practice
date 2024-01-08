class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()

        return " ".join(reversed(words))
        

        '''
        Extract the words sepearted by a space into an array

        reverse our list, and join on " "
        '''
