class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # min stack logic
        if not self.minstack:
            self.minstack.append(val)
        else:
            if val < self.minstack[-1]:
                self.minstack.append(val)
            else:
                # keep previous value if not smaller
                self.minstack.append(self.minstack[-1])


    def pop(self) -> None:
        self.stack.pop()

        # min stack logic
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        

'''
2 stacks: 1 will be standard that we use 'stack'; 'minstack' also taht we also populate

1: 1 2 3
2: 1 1 1
'''

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
