class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','i','o','u'])

        result = 0

        # window
        left = 0
        right = 0

        # make our window
        vowels_window = 0

        for i in range(0,k):
            if s[i] in vowels:
                vowels_window += 1
            
            right += 1
        
        result = max(result,vowels_window) # potential candidate
        
        # shift our window
        while right < len(s):
            if s[right] in vowels:
                vowels_window += 1 # add a vowel to window
            
            # handle case where we lose a vowel
            if s[left] in vowels:
                vowels_window -= 1
            
            right += 1
            left += 1

            # check if greater than result
            result = max(result,vowels_window)


        return result



'''
hashset with vowels

make a window length k
    - keep track of how many vowels we have

as we move it
    - decrement if we lose a vowel
    - increment if we gain a vowel
'''
