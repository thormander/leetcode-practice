class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carSorted = sorted(zip(position,speed))

        stack = []
        result = 0

        # fill stack with time to target
        for pair in carSorted:
            timeTaken = (target - pair[0]) / pair[1]
            stack.append(timeTaken)
        
        # figure out which car is fleet
        while len(stack) > 1:
            frontCarSpeed = stack.pop()

            if frontCarSpeed < stack[-1]:
                result += 1
            else:
                stack[-1] = frontCarSpeed
    
        if stack:
            result += 1

        return result

'''
position = [10,8,0,5,3], speed = [2,4,1,1,3]

1. pair (postion,speed)
2. sort off position

[(0,1),(3,3),(5,1),(8,4),(10,2)]
                    |

time taken to get to target = (target - cur_position) / cur_speed

[12,3,7,1,1]

stack = [12]

if popped < top of stack:
    result++
else:
    top of stack now equal to popped (ie the same speed or slower car)

if stack not empty
    add 1

result = 3
'''
