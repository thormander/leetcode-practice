class Solution:
    def isPalindrome(self, s: str) -> bool:

        # pointers
        left = 0
        right = len(s) - 1

        # stop after they collide
        while left < right:
            # first check if its a valid char
            if not (ord("a") <= ord(s[left].lower()) <= ord("z") or ord("0") <= ord(s[left].lower()) <= ord("9")):
                left += 1
                continue
            if not (ord("a") <= ord(s[right].lower()) <= ord("z") or ord("0") <= ord(s[right].lower()) <= ord("9")):
                right -= 1
                continue

            if (s[left].lower() != s[right].lower()):
                return False
            else:
                left += 1
                right -= 1
        
        return True



        

'''
we can use 2 pointers: one at start, one at end

compare the char at both pointers: but...
    make sure it is lowercase,
    ** need to make sure it is actually a char ** 
        - otherwise we increment/decrement our pointer
'''
