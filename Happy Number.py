class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        while True:
            hashset.add(n)
            
            # do the sum
            n = self.sumSquare(n)

            if n == 1:
                return True
            elif n in hashset:
                return False
            
        
    def sumSquare(self,n: int) -> int:
        total = 0
        
        while n != 0:
            num = n % 10
            total += num * num
            n = n // 10 # we know we are done when this is 0
        
        return total


        

        




        
'''
2 outcomes:
 - it can loop forever --> return false
 - or it ends on 1 exactly --> return true

hashset --> to find if we are going to cycle

Some tricks to do the sum of squares

19 % 10 = 9 first place
total + 9^2
19 // 10 =  1
'''
