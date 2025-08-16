class MinStack:

    def __init__(self):
        self.minstack = []
        self.trackMin = []
        

    def push(self, val: int) -> None:
        self.minstack.append(val)

        if not self.trackMin:
            self.trackMin.append(val)
        else:
            if self.trackMin[-1] > val:
                self.trackMin.append(val) # append new value if current IS smaller
            else:
                self.trackMin.append(self.trackMin[-1]) # append previous value if current not smaller
        

    def pop(self) -> None:
        self.minstack.pop()
        self.trackMin.pop()
        

    def top(self) -> int:
        return self.minstack[-1]
        

    def getMin(self) -> int:
        return self.trackMin[-1]

        
'''
[1,2,0,3] -3 end result stack
           |
[1,2,0,3] min stack
[1,1,0,0] min tracking

need a way to track the minimum in our stack, and update as we pop/add
'''

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
