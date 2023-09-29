class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0 # hold our paindrome substrings count
        
        def isPalindrome(left,right):
            result = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # we have a valid palindrome
                result += 1

                left -= 1
                right += 1 
            return result             

        for i in range(len(s)):
            
            # odd sized
            left = i
            right = i
            result += isPalindrome(left,right)
            
            # even sized
            left = i
            right = i + 1
            result += isPalindrome(left,right)
               
        return result

        '''
        palindrome? --> start at middle, and go out.
        '''
        
