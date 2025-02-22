class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()

        return " ".join(words)


'''
extract words out (basically seperate based on whitespce) --> .split()

reverse order and put a space between
'''
