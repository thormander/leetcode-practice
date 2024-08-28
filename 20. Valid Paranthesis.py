class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {')':'(','}':'{',']':'['}

        for char in s:
            # check if opening par
            if char in pairs.values():
                stack.append(char)
                continue
            else:
                # closing
                # base case
                if not stack:
                    return False
                else:
                    if stack[-1] == pairs[char]:
                        stack.pop()
                        continue
                    else:
                        return False

        
        if stack:
            return False
        else:
            return True

'''
stack
 - where as we find pairs, remove from stack...
 - if our stack is empty, that means we return true (each parantehse has a pair)

dictionary: what pairs with what

loop through
 - if its opening, just add to stack and keep goin
 - if we run into a closing, check top of our stack and see if the are a pair and remove if they are

'''
