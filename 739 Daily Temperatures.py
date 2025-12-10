class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index,temp in enumerate(temperatures):
            if not stack:
                stack.append((temp,index))
                continue
            
            while stack and (temp > stack[-1][0]):
                poppedTuple = stack.pop()
                result[poppedTuple[1]] = index - poppedTuple[1]

            stack.append((temp,index))
        
        return result




'''
[30,40,50,30,60]
    |

[1,0,0,0]

[(30,0)]
'''
