class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        hashsetNumIsOdd = {'b','d','f','h'} # land on white when odd
        hashsetNumIsEven = {'a','c','e','g'} # land on white when even

        if int(coordinates[1]) % 2 != 0:
            # case of odd
            if coordinates[0] in hashsetNumIsOdd:
                return True
            else:
                return False
        else:
            # case of even
            if coordinates[0] in hashsetNumIsEven:
                return True
            else:
                return False


'''
give a string with coords on it
letter always first, number second such as (a1, or b2)

determine if it is white or black (if white then true otherwise false)
 - find what determines when a color is white

Look at index 1, is number even or odd?

if odd:
    white will be on b,d,f, or h
    return True if white or false if black
else:
    white will be on a,c,e, or g
    return True if white or false if black

store in hashset our odd or even list.
'''
