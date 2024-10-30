class Solution:
    def getSmallestString(self, s: str) -> str:

        result = list(s)

        left = 0
        right = 1

        while right < len(s):

            # case where we can swap
            if int(s[left]) % 2 == int(s[right]) % 2 and s[right] < s[left]: # if both even/odd
                result[left] = s[right]
                result[right] = s[left]
                # immeadeatly return b/c we can only do one swap
                return ''.join(result)
            # increment our points
            left += 1
            right += 1
        
        return s


'''
consider smaller int is smaller --> lexographically smaller

one swap at most
 - one choice, so ideal would be to swap near beginning of the string

 - swapping at the front would be the best as it will result in a overall smaller change if possible.
 - if not, we can move to the next adjacent pair and see if we can swap.

2 pointers
 - index 0, index 1

check if these 2 are the same parity
 - if they are, do the swap ONLY if right is less than left
    - return this as the answer
 - for all other cases, just increment both are pointers

if no swaps jsut return the original string
'''
