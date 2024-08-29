class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i,v in enumerate(temperatures):
            
            while stack and stack[-1][1] < v:
                temp = stack.pop() # pop [i,v] from top stack
                # populate position of popped temp with time to wait
                answer[temp[0]] = i - temp[0]

            stack.append([i,v])
        
        return answer





'''
[1,1,1,0] answer
[[0,30]] stack
'''
        
