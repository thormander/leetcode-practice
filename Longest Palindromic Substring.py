class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = ""
        lenLongest = 0
        lengthInput = len(s)

        for i in range(lengthInput):
            # odd case
            left = i
            right = i
            while left >= 0 and right < lengthInput and s[left] == s[right]:
                # found a palindrome
                if (right - left + 1) > lenLongest:
                    longest = s[left:right+1]
                    lenLongest = (right - left + 1)
                
                left -= 1
                right += 1

            # even case
            left = i
            right = i + 1
            while left >= 0 and right < lengthInput and s[left] == s[right]:
                # found a palindrome
                if (right - left + 1) > lenLongest:
                    longest = s[left:right+1]
                    lenLongest = (right - left + 1)
                
                left -= 1
                right += 1
                        
        return longest


        
            
            
