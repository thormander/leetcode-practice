class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            # is pointer on a alpha numeric character
            while left <= right and not s[left].isalnum():
                left += 1
            while right >= left and not s[right].isalnum():
                right -= 1
            
            # do the comparison
            if left <= right and s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True


'''
1. clean up original string
    - upper to lower
    - remove commas, colons, ...
2. get rid of spaces
3. 2 pointer check

-------
more effcient
 - start with 2 points
 - first make sure its an actual letter
    - if they are make it lower case and compare the 2
    - skip any non letters, up until we hit another letter
'''
