class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = [] # [[temp,index],....]

        for i,v in enumerate(temperatures):
            # check if greater that top of stack
            while stack and stack[-1][0] < v:
                poppedTemp, poppedIndex = stack.pop()
                result[poppedIndex] = i - poppedIndex
        
            stack.append([v,i])
        
        return result



        


'''
result[i] == amt of days till it gets warmer, otherwise 0

[30,40,50,30,60]
              |
[1,1,2,1,0]

stack = [[60,4]]

'''
