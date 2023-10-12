class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []
        

        #backtrack
        def DFS(i):
            # base case
            if i >= len(s):
                result.append(partition.copy())
                return
            
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    partition.append(s[i:j+1])
                    DFS(j+1) # if it is, we can continue searching
                    partition.pop()
                else:
                    continue

        DFS(0)
        return result
        
    # helper
    def isPalindrome(self, s, i, j):
        s_to_check = s[i:j+1]
        return s_to_check == s_to_check[::-1]
        

