class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # check collision
            while stack and (stack[-1] > 0 and a < 0):
                top_a = stack.pop()
                if top_a + a == 0:
                    # same size asteroid, dont add new one and remove old one
                    break
                if top_a + a > 0:
                    # keep old asteroid, new asteroid broke
                    stack.append(top_a)
                    break
                # also handles case where new ast bigger, which is handled as we popped already
            
            else:
                # if we dont go into the while
                stack.append(a)
        
        return stack



'''
all we need to worry about is collisions

if we start with negs, they will never collide with a pos on the irght

use a stack for this, and check top everytime we get a new asteroid
'''
