class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        while n not in hashset:
            hashset.add(n)

            n = self.sumSquares(n)

            if n == 1:
                return True
        return False

    def sumSquares(self, n: int) -> int:
        total = 0
        while n != 0:
            num = n % 10
            total += num * num # square
            n = n // 10 # interger division
        return total



        
'''
what is happy? --> after split and adding, if we get 1 return true otherwside false

logic for the split and addtion
 - modulo to extract single number
 - division by 10 to go the the next number place

n = 2

2^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
... 
use a hashset to store these values and check if we get a repeat. --> when we can stop our loop
'''
