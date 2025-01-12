class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        def self_dividing(num: int) -> bool:
            string_num = str(num)
            for char in string_num:
                if char == '0' or num % int(char) != 0:
                    return False
            
            return True

        for i in range(left,right + 1):
            if self_dividing(i) == True:
                result.append(i)
        
        return result
            



'''
range between left and right INCLUSIVE

helper function --> boolean
    check if its self dividing
'''
