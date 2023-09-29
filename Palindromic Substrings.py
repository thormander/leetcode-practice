class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0 # hold our paindrome substrings count
        
        for i in range(len(s)):
            
            # odd sized
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # we have a valid palindrome
                result += 1

                left -= 1
                right += 1
            
            # even sized
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # we have a valid palindrome
                result += 1

                left -= 1
                right += 1
                
            
        return result

        '''
        palindrome? --> start at middle, and go out.
        '''
        
