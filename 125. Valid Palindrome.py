class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left <= right:
            # left
            while left < right and s[left].isalnum() == False:
                # skip non valid chars
                left += 1

            # right
            while left < right and s[right].isalnum() == False:
                # skip non valid chars
                right -= 1
            
            # compare
            if s[left].lower() != s[right].lower():
                return False

            # if equal just move the pointers
            left += 1
            right -= 1
            
        return True

'''
make sure we are comparing the right letters/numbers
    - also skip non valid characters

2 pointers
    - at the start and end of the string


"Race a car"
    | |


Cases to skip:
    - is it nonvalid char

compare
    - both same case
    - and our pointers aren't crossed

'''
