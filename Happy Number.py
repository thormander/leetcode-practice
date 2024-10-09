class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        while n not in hashset:
            hashset.add(n)

            calc = 0
            while n != 0:
                num = n % 10
                calc += (num * num) # add the square
                n = n // 10
            
            if calc == 1:
                return True

            n = calc 
        
        return False


