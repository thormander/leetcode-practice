class Solution:
    def climbStairs(self, n: int) -> int:
        right = 1 # starting at n
        left = 1 # starting at n-1

        for i in range(n-1):
            temp = left
            left = left + right
            right = temp
        
        return left

        '''
        DP; use 2 variables starting at one

        why one?
            when at n, there is only one way from n-1
            when at n-1, there is only one way to get to n

        just loop through n-1 times (b/c we have a variable starting at n-1) and add the 2 variables togetherr:
            think of we start at the end with 2 pointers and shift both left until we get to the end
        '''
