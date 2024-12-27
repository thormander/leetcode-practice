class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        temp_p = []

        def backtrack(index):
            if index >= len(s):
                result.append(temp_p.copy())
                return
            
            for j in range(index,len(s)):
                if self.is_palindrome(s[index:j+1]) == True:
                    temp_p.append(s[index:j+1])
                    backtrack(j+1)
                    temp_p.pop()
        
        backtrack(0)
        return result
        
    def is_palindrome(self, s):
        # 2 pointer methdo
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True        



'''
helper function returns T/F if its a palindrome

"aab"

a      aa aab
| \     | 
a  ab  b
|
b

partition tree partition(index):
    base case, if our index is out of bounds, add that partition

    go through every other character not on index:
        if index --> j in s is a palindrome:
            add to results
            recurse and increment index
            pop the partition to clean up

'''
