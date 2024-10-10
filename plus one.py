class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        right = len(digits) - 1

        # traverse array in reverse
        while right >= 0:
            # normal case (ie. when we dont have carry overs)
            if digits[right] != 9:
                digits[right] += 1
                return digits
            
            # case if we have 9 and need to handle carry over
            digits[right] = 0
            right -=1
        
        # if we get to this point without returning, that means array was all 9s
        digits.insert(0,1)
        return digits
