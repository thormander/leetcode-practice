class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = ""

        # clean up string s
        for char in s:
            if (ord('a') <= ord(char.lower()) <= ord('z')):
                clean += char.lower()
            elif (ord('0') <= ord(char) <= ord('9')):
                clean += char
            else:
                continue

        left = 0
        right = len(clean) - 1
        
        # check palindrome
        while left < right:
            if clean[left] != clean[right]:
                return False
            else:
                left += 1
                right -= 1
                continue
        
        return True


'''
make sure we are using lowercase
skip any / remove non alphanumeric characters

it CAN include numbers
'''
