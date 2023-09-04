class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1            
            if s[left].lower() != s[right].lower():
                return False
            # need to update pointers after comparison
            left += 1
            right -= 1
        
        return True


        '''
        ignore non alphanumeric, and compare left and right pointers

        while:
            need to skip over any nonnumeric
            return false when left != right

        '''
