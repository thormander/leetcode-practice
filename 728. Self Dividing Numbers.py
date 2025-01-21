class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        # help function to determine if self dividing
        def dividing(number: int) -> bool:
            for char in str(number):
                if char == '0' or number % int(char) != 0:
                    return False
            return True

        for number in range(left,right+1):
            if dividing(number) == True:
                result.append(number)
        
        return result


'''
helper function:
    what is a self diving nubmer? return true false
    converting the integer to a string and iterating through it

iterate between lef4t and right and check if the number is self dividing

'''
        
